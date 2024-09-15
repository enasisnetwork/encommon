"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from ast import literal_eval as leval
from contextlib import suppress
from re import DOTALL
from re import findall as re_findall
from re import match as re_match
from typing import Any
from typing import Callable
from typing import Optional

from jinja2 import Environment
from jinja2 import StrictUndefined

from ..colors import Color
from ..crypts import Hashes
from ..times import Duration
from ..times import Time
from ..types import DictStrAny
from ..types import fuzzy_list
from ..utils import fuzz_match
from ..utils import rgxp_match



FILTER = Callable[..., Any]

JINJA2 = (
    r'(\{\{.+?\}\})|'
    r'(\{\%.+?\%\})')

LITERAL = (
    r'^((\{([^\{%].+?)?\})|(\[(.+?|)\])'
    '|True|False|None|'
    r'(\-?([1-9]\d*|0)(\.\d+)?))$')

DEFAULT: dict[str, FILTER] = {
    'Duration': Duration,
    'Color': Color,
    'Hashes': Hashes,
    'Time': Time,
    'fuzz_match': fuzz_match,
    'fuzzy_list': fuzzy_list,
    'rgxp_match': rgxp_match}



class Jinja2:
    """
    Parse the provided input and intelligently return value.

    Example
    -------
    >>> jinja2 = Jinja2()
    >>> jinja2.parse('{{ 0 | Time}}')
    '1970-01-01T00:00:00.000000+0000'

    :param statics: Additional values available for parsing.
    :param filters: Additional filter functions for parsing.
    """

    __statics: DictStrAny
    __filters: dict[str, FILTER]

    __jinjenv: Environment


    def __init__(
        self,
        statics: Optional[DictStrAny] = None,
        filters: Optional[dict[str, FILTER]] = None,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        statics = dict(statics or {})
        filters = dict(filters or {})

        items = DEFAULT.items()

        for key, filter in items:
            filters[key] = filter

        self.__statics = statics
        self.__filters = filters

        jinjenv = Environment(
            auto_reload=False,
            autoescape=False,
            cache_size=0,
            extensions=[
                'jinja2.ext.i18n',
                'jinja2.ext.loopcontrols',
                'jinja2.ext.do'],
            keep_trailing_newline=False,
            lstrip_blocks=False,
            newline_sequence='\n',
            optimized=True,
            trim_blocks=False,
            undefined=StrictUndefined)

        jinjenv.filters |= filters

        self.__jinjenv = jinjenv


    @property
    def statics(
        self,
    ) -> DictStrAny:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return dict(self.__statics)


    @property
    def filters(
        self,
    ) -> dict[str, FILTER]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return dict(self.__filters)


    @property
    def jinjenv(
        self,
    ) -> Environment:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.__jinjenv


    def parser(
        self,
        value: str,
        statics: Optional[DictStrAny] = None,
    ) -> Any:
        """
        Return the provided input using the Jinja2 environment.

        :param value: Input that will be processed and returned.
        :param statics: Additional values available for parsing.
        :returns: Provided input using the Jinja2 environment.
        """

        statics = statics or {}

        parser = (
            self.__jinjenv
            .from_string)

        rendered = (
            parser(value)
            .render(**statics))

        return rendered


    def parse(  # noqa: CFQ004
        self,
        value: Any,
        statics: Optional[DictStrAny] = None,
        literal: bool = True,
    ) -> Any:
        """
        Return the provided input using the Jinja2 environment.

        :param value: Input that will be processed and returned.
        :param statics: Additional values available for parsing.
        :param literal: Determine if Python objects are evaled.
        :returns: Provided input using the Jinja2 environment.
        """


        def _final(  # noqa: CFQ004
            value: Any,
        ) -> Any:

            if literal is False:
                return value

            match = re_match(
                LITERAL, str(value))

            if match is None:
                return value

            with suppress(Exception):
                return leval(value)

            return value


        def _parse(
            value: Any,
        ) -> Any:

            return self.parse(
                value,
                statics, literal)


        def _parser(
            value: Any,
        ) -> Any:

            parsed = self.parser(
                value, statics)

            return _final(parsed)


        def _found(
            value: Any,
        ) -> list[Any]:

            value = str(value)

            return re_findall(
                JINJA2, value, DOTALL)


        if not len(_found(value)):
            return _final(value)


        with suppress(Exception):
            value = _final(value)


        if isinstance(value, dict):

            value = dict(value)

            items = value.items()

            for key, _value in items:

                _value = _parse(_value)

                value[key] = _value


        elif isinstance(value, list):

            value = list(value)

            values = enumerate(value)

            for idx, _value in values:

                _value = _parse(_value)

                value[idx] = _value


        elif value is not None:
            value = _parser(value)


        return value