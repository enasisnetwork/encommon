"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from copy import deepcopy
from threading import Lock
from typing import Optional
from typing import TYPE_CHECKING
from typing import Type

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from .common import PARSABLE
from .params import TimersParams
from .time import Time
from .timer import Timer
from ..types import DictStrAny

if TYPE_CHECKING:
    from .params import TimerParams



TIMERS = dict[str, Timer]



class TimersTable(DeclarativeBase):
    """
    Schematic for the database operations using SQLAlchemy.

    .. note::
       Fields are not completely documented for this model.
    """

    group = Column(
        String,
        primary_key=True,
        nullable=False)

    unique = Column(
        String,
        primary_key=True,
        nullable=False)

    last = Column(
        String,
        nullable=False)

    update = Column(
        String,
        nullable=False)



class Timers:
    """
    Track timers on unique key determining when to proceed.

    .. warning::
       This class will use an in-memory database for cache,
       unless a cache file is explicity defined.

    .. testsetup::
       >>> from .params import TimerParams
       >>> from .params import TimersParams
       >>> from time import sleep

    Example
    -------
    >>> source = {'one': TimerParams(timer=1)}
    >>> params = TimersParams(timers=source)
    >>> timers = Timers(params)
    >>> timers.ready('one')
    False
    >>> sleep(1)
    >>> timers.ready('one')
    True

    :param params: Parameters used to instantiate the class.
    :param store: Optional database path for keeping state.
    :param group: Optional override for default group name.
    """

    __params: 'TimersParams'

    __store: str
    __group: str
    __table: Type[TimersTable]
    __locker: Lock

    __sengine: Engine
    __session: (
        # pylint: disable=unsubscriptable-object
        sessionmaker[Session])

    __childs: TIMERS


    def __init__(
        self,
        params: Optional['TimersParams'] = None,
        *,
        store: str = 'sqlite:///:memory:',
        table: str = 'timers',
        group: str = 'default',
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        params = deepcopy(params)

        if params is None:
            params = TimersParams()

        self.__params = params


        self.__store = store
        self.__group = group

        class SQLBase(DeclarativeBase):
            pass

        self.__table = type(
            f'encommon_timers_{table}',
            (SQLBase, TimersTable),
            {'__tablename__': table})

        self.__locker = Lock()

        self.__build_engine()


        self.__childs = {}

        self.load_children()


    def __build_engine(
        self,
    ) -> None:
        """
        Construct instances using the configuration parameters.
        """

        sengine = create_engine(
            self.__store,
            pool_pre_ping=True)

        (self.__table.metadata
         .create_all(sengine))

        session = (
            sessionmaker(sengine))

        self.__sengine = sengine
        self.__session = session


    @property
    def params(
        self,
    ) -> 'TimersParams':
        """
        Return the Pydantic model containing the configuration.

        :returns: Pydantic model containing the configuration.
        """

        return self.__params


    @property
    def store(
        self,
    ) -> str:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.__store


    @property
    def group(
        self,
    ) -> str:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.__group


    @property
    def store_table(
        self,
    ) -> Type[TimersTable]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.__table


    @property
    def store_engine(
        self,
    ) -> Engine:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.__sengine


    @property
    def store_session(
        self,
    ) -> Session:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.__session()


    @property
    def children(
        self,
    ) -> dict[str, Timer]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return dict(self.__childs)


    def load_children(
        self,
    ) -> None:
        """
        Construct the children instances for the primary class.
        """

        params = self.__params
        timers = self.__childs

        group = self.__group

        session = self.store_session

        config = params.timers


        table = self.__table
        _group = table.group
        _unique = table.unique

        query = (
            session.query(table)
            .filter(_group == group)
            .order_by(_unique))

        for record in query.all():

            unique = str(record.unique)
            last = str(record.last)

            if unique not in config:
                continue

            _config = config[unique]

            _config.start = last


        items = config.items()

        for key, value in items:

            if key in timers:

                timer = timers[key]

                timer.update(value.start)

                continue

            timer = Timer(
                value.timer,
                start=value.start)

            timers[key] = timer


        self.__childs = timers


    def save_children(
        self,
    ) -> None:
        """
        Save the child caches from the attribute into database.
        """

        sess = self.__session()
        lock = self.__locker

        table = self.__table
        group = self.__group
        childs = self.__childs


        inserts: list[DictStrAny] = []

        update = Time('now')


        items = childs.items()

        for unique, cache in items:

            _last = cache.time.subsec
            _update = update.subsec

            inputs: DictStrAny = {
                'group': group,
                'unique': unique,
                'last': _last,
                'update': _update}

            inserts.append(inputs)


        with lock, sess as session:

            for insert in inserts:

                session.merge(
                    table(**insert))

            session.commit()


    def ready(
        self,
        unique: str,
        update: bool = True,
    ) -> bool:
        """
        Determine whether or not the appropriate time has passed.

        :param unique: Unique identifier for the related child.
        :param update: Determines whether or not time is updated.
        :returns: Boolean indicating whether enough time passed.
        """

        childs = self.__childs

        if unique not in childs:
            raise ValueError('unique')

        child = childs[unique]

        ready = child.ready(update)

        if ready is True:
            self.save_children()

        return ready


    def pause(
        self,
        unique: str,
        update: bool = True,
    ) -> bool:
        """
        Determine whether or not the appropriate time has passed.

        :param unique: Unique identifier for the related child.
        :param update: Determines whether or not time is updated.
        :returns: Boolean indicating whether enough time passed.
        """

        return not self.ready(
            unique, update)


    def create(
        self,
        unique: str,
        params: 'TimerParams',
    ) -> Timer:
        """
        Create a new timer using the provided input parameters.

        :param unique: Unique identifier for the related child.
        :param params: Parameters used to instantiate the class.
        :returns: Newly constructed instance of related class.
        """

        childs = self.__childs
        _params = self.params

        config = _params.timers

        if unique in config:
            raise ValueError('unique')

        config[unique] = params

        self.load_children()

        self.save_children()

        return childs[unique]


    def update(
        self,
        unique: str,
        value: Optional[PARSABLE] = None,
    ) -> None:
        """
        Update the timer from the provided parasable time value.

        :param unique: Unique identifier for the related child.
        :param value: Override the time updated for timer value.
        """

        childs = self.__childs

        if unique not in childs:
            raise ValueError('unique')

        child = childs[unique]

        child.update(value)

        self.save_children()


    def delete(
        self,
        unique: str,
    ) -> None:
        """
        Delete the timer from the internal dictionary reference.

        .. note::
           This is a graceful method, will not raise exception
           when the provided unique value does not exist.

        :param unique: Unique identifier for the related child.
        """

        sess = self.__session()
        lock = self.__locker

        table = self.__table
        group = self.__group

        _unique = table.unique
        _group = table.group


        with lock, sess as session:

            (session.query(table)
             .filter(_unique == unique)
             .filter(_group == group)
             .delete())

            session.commit()


        params = self.__params
        config = params.timers

        params = self.__params
        childs = self.__childs

        if unique in config:
            del config[unique]

        if unique in childs:
            del childs[unique]
