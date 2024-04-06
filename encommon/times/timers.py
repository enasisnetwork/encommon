"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from sqlite3 import connect as SQLite
from typing import Optional
from typing import TYPE_CHECKING

from .common import NUMERIC
from .common import PARSABLE
from .times import Times

if TYPE_CHECKING:
    from sqlite3 import Connection



CACHE_TABLE = (
    """
    create table if not exists
     {0} (
      "unique" text not null,
      "update" text not null,
     primary key ("unique"));
    """)  # noqa: LIT003



_TIMERS = dict[str, float]
_CACHED = dict[str, Times]



class Timers:
    """
    Track timers on unique key and determine when to proceed.

    .. warning::
       This class will use an in-memory database for cache,
       unless a cache file is explicity defined.

    .. testsetup::
       >>> from time import sleep

    Example
    -------
    >>> timers = Timers({'one': 1})
    >>> timers.ready('one')
    False
    >>> sleep(1)
    >>> timers.ready('one')
    True

    :param timers: Seconds that are used for each of timers.
    :param cache_file: Optional path to SQLite database for
        cache. This will allow for use between executions.
    :param cache_name: Optional override default table name.
    """

    __timers: _TIMERS
    __sqlite: 'Connection'
    __table: str
    __cached: _CACHED


    def __init__(
        self,
        timers: Optional[dict[str, NUMERIC]] = None,
        cache_file: str = ':memory:',
        cache_name: str = 'encommon_timers',
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """


        timers = dict(timers or {})

        items = timers.items()

        for key, value in items:
            timers[key] = float(value)


        sqlite = SQLite(cache_file)

        sqlite.execute(
            CACHE_TABLE
            .format(cache_name))

        sqlite.commit()


        cached: _CACHED = {}

        for timer in timers:
            cached[timer] = Times()


        self.__timers = timers
        self.__sqlite = sqlite
        self.__table = cache_name
        self.__cached = cached


        self.load_cache()
        self.save_cache()


    def load_cache(
        self,
    ) -> None:
        """
        Load the timers cache from the database into attribute.
        """

        cached = self.__sqlite
        table = self.__table
        cachem = self.__cached

        cursor = cached.execute(
            f'select * from {table}'
            ' order by "unique" asc')

        records = cursor.fetchall()

        for record in records:

            unique = record[0]
            update = record[1]

            times = Times(update)

            cachem[unique] = times


    def save_cache(
        self,
    ) -> None:
        """
        Save the timers cache from the attribute into database.
        """

        insert = tuple[str, str]
        inserts: list[insert] = []


        cached = self.__sqlite
        table = self.__table
        cachem = self.__cached


        items = cachem.items()

        for key, value in items:

            append = (key, str(value))

            inserts.append(append)


        cached.executemany(
            (f'replace into {table}'
             ' ("unique", "update")'
             ' values (?, ?)'),
            tuple(sorted(inserts)))

        cached.commit()


    @property
    def timers(
        self,
    ) -> _TIMERS:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return dict(self.__timers)


    @property
    def cache_file(
        self,
    ) -> 'Connection':
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.__sqlite


    @property
    def cache_name(
        self,
    ) -> str:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.__table


    @property
    def cache_dict(
        self,
    ) -> _CACHED:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return dict(self.__cached)


    def ready(
        self,
        unique: str,
        update: bool = True,
    ) -> bool:
        """
        Determine whether or not the appropriate time has passed.

        .. note::
           For performance reasons, this method will not notice
           changes within the database unless refreshed first.

        :param unique: Which timer configuration from reference.
        :param update: Determines whether or not time is updated.
        """

        timers = self.__timers
        caches = self.__cached

        if unique not in caches:
            raise ValueError('unique')

        cache = caches[unique]
        timer = timers[unique]

        ready = cache.since >= timer

        if ready and update:
            self.update(unique)

        return ready


    def update(
        self,
        unique: str,
        started: Optional[PARSABLE] = None,
    ) -> None:
        """
        Update the existing timer from mapping within the cache.

        :param unique: Which timer configuration from reference.
        :param started: Override the start time for timer value.
        """

        caches = self.__cached

        if unique not in caches:
            raise ValueError('unique')

        caches[unique] = Times(started)

        self.save_cache()


    def create(
        self,
        unique: str,
        minimum: int | float,
        started: Optional[PARSABLE] = None,
    ) -> None:
        """
        Update the existing timer from mapping within the cache.

        :param unique: Which timer configuration from reference.
        :param minimum: Determine minimum seconds that must pass.
        :param started: Determine when time starts for the timer.
        """

        timers = self.__timers
        caches = self.__cached

        if unique in timers:
            raise ValueError('unique')

        timers[unique] = float(minimum)
        caches[unique] = Times(started)

        self.save_cache()
