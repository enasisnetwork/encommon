"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Literal
from typing import Union



DURAGROUP = Literal[
    'year', 'month', 'week',
    'day', 'hour', 'minute',
    'second']

DURASHORT = {
    'year': 'y',
    'month': 'mon',
    'week': 'w',
    'day': 'd',
    'hour': 'h',
    'minute': 'm',
    'second': 's'}



class Duration:
    """
    Convert provided the seconds into a human friendly format.

    Example
    -------
    >>> Duration(86400 * 700).compact
    '1y11mon5d'

    Example
    -------
    >>> Duration(86400 * 700).verbose
    '1 year, 11 months, 5 days'

    Example
    -------
    >>> Duration(7201, False).verbose
    '2 hours, 1 second'

    :param seconds: Period in seconds that will be iterated.
    :param smart: Determines if we hide seconds after minute.
    """

    __source: float
    __smart: bool


    def __init__(
        self,
        seconds: int | float,
        smart: bool = True,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        self.__source = float(seconds)
        self.__smart = bool(smart)


    def __repr__(
        self,
    ) -> str:
        """
        Built-in method for representing the values for instance.

        :returns: String representation for values from instance.
        """

        return f'Duration({self.source}, {self.smart})'


    def __hash__(
        self,
    ) -> int:
        """
        Built-in method called when performing hashing operation.

        :returns: Boolean indicating outcome from the operation.
        """

        return int(self.__source * 100000)


    def __str__(
        self,
    ) -> str:
        """
        Built-in method for representing the values for instance.

        :returns: String representation for values from instance.
        """

        return self.compact


    def __int__(
        self,
    ) -> int:
        """
        Built-in method representing numeric value for instance.

        :returns: Numeric representation for values from instance.
        """

        return int(self.__source)


    def __float__(
        self,
    ) -> float:
        """
        Built-in method representing numeric value for instance.

        :returns: Numeric representation for values from instance.
        """

        return float(self.__source)


    def __add__(
        self,
        other: Union['Duration', int, float],
    ) -> float:
        """
        Built-in method for mathematically processing the value.

        :param other: Other value being compared with instance.
        :returns: Python timedelta object containing the answer.
        """

        if hasattr(other, 'source'):
            other = other.source

        return self.__source + other


    def __sub__(
        self,
        other: Union['Duration', int, float],
    ) -> float:
        """
        Built-in method for mathematically processing the value.

        :param other: Other value being compared with instance.
        :returns: Python timedelta object containing the answer.
        """

        if hasattr(other, 'source'):
            other = other.source

        return self.__source - other


    def __eq__(
        self,
        other: object,
    ) -> bool:
        """
        Built-in method for comparing this instance with another.

        :param other: Other value being compared with instance.
        :returns: Boolean indicating outcome from the operation.
        """

        if hasattr(other, 'source'):
            other = other.source

        return self.__source == other


    def __ne__(
        self,
        other: object,
    ) -> bool:
        """
        Built-in method for comparing this instance with another.

        :param other: Other value being compared with instance.
        :returns: Boolean indicating outcome from the operation.
        """

        return not self.__eq__(other)


    def __gt__(
        self,
        other: Union['Duration', int, float],
    ) -> bool:
        """
        Built-in method for comparing this instance with another.

        :param other: Other value being compared with instance.
        :returns: Boolean indicating outcome from the operation.
        """

        if hasattr(other, 'source'):
            other = other.source

        return self.__source > other


    def __ge__(
        self,
        other: Union['Duration', int, float],
    ) -> bool:
        """
        Built-in method for comparing this instance with another.

        :param other: Other value being compared with instance.
        :returns: Boolean indicating outcome from the operation.
        """

        if hasattr(other, 'source'):
            other = other.source

        return self.__source >= other


    def __lt__(
        self,
        other: Union['Duration', int, float],
    ) -> bool:
        """
        Built-in method for comparing this instance with another.

        :param other: Other value being compared with instance.
        :returns: Boolean indicating outcome from the operation.
        """

        if hasattr(other, 'source'):
            other = other.source

        return self.__source < other


    def __le__(
        self,
        other: Union['Duration', int, float],
    ) -> bool:
        """
        Built-in method for comparing this instance with another.

        :param other: Other value being compared with instance.
        :returns: Boolean indicating outcome from the operation.
        """

        if hasattr(other, 'source'):
            other = other.source

        return self.__source <= other


    @property
    def source(
        self,
    ) -> float:
        """
        Return the property for attribute from the class instance.

        :returns: Property for attribute from the class instance.
        """

        return self.__source


    @property
    def smart(
        self,
    ) -> bool:
        """
        Return the property for attribute from the class instance.

        :returns: Property for attribute from the class instance.
        """

        return self.__smart


    @property
    def groups(
        self,
    ) -> dict[DURAGROUP, int]:
        """
        Return the groups of time units with each relevant value.

        :returns: Groups of time units with each relevant value.
        """

        seconds = int(self.__source)

        returned: dict[DURAGROUP, int] = {}

        groups: dict[DURAGROUP, int] = {
            'year': 31536000,
            'month': 2592000,
            'week': 604800,
            'day': 86400,
            'hour': 3600,
            'minute': 60}

        for key, value in groups.items():

            if seconds < value:
                continue

            _value = seconds // value

            returned[key] = _value

            seconds %= value

        if seconds >= 1:
            returned['second'] = seconds

        return returned


    @property
    def compact(
        self,
    ) -> str:
        """
        Return the compact format calculated from source duration.

        :returns: Compact format calculated from source duration.
        """

        parts: list[str] = []

        source = self.__source
        groups = self.groups

        for part, value in groups.items():

            if (part == 'second'
                    and self.__smart
                    and source >= 60):
                continue

            unit = DURASHORT[part]

            parts.append(f'{value}{unit}')

        return ''.join(parts)


    @property
    def verbose(
        self,
    ) -> str:
        """
        Return the verbose format calculated from source duration.

        :returns: Compact format calculated from source duration.
        """

        parts: list[str] = []

        source = self.__source
        groups = self.groups

        if source < 60:
            return 'just now'

        for part, value in groups.items():

            if (part == 'second'
                    and self.__smart
                    and source >= 60):
                continue

            unit = (
                f'{part}s'
                if value != 1
                else part)

            parts.append(f'{value} {unit}')

        return ', '.join(parts)
