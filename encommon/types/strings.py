"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Any



COMMAS = ', '
COMMAD = ','

NEWLINE = '\n'

SEMPTY = ''
SPACED = ' '



def striplower(
    value: str,
) -> str:
    """
    Return the provided string but stripped and lower cased.

    Example
    -------
    >>> striplower('  Foo ')
    'foo'

    :param value: String which will be stripped and lowered.
    :returns: Provided string but stripped and lower cased.
    """

    return value.strip().lower()



def hasstr(
    haystack: str,
    needle: str,
) -> bool:
    """
    Return the boolean indicating if needle is in haystack.

    Example
    -------
    >>> haystack = 'barfoobaz'
    >>> needle = 'foo'
    >>> hasstr(haystack, needle)
    True

    :param haystack: Full string which may contain needle.
    :param needle: Substring which may be within haystack.
    :returns: Boolean indicating if needle is in haystack.
    """

    return needle in haystack



def inrepr(
    needle: str,
    haystack: Any,  # noqa: ANN401
) -> bool:
    """
    Return the boolean indicating if needle is in haystack.

    Example
    -------
    >>> class MyClass: pass
    >>> haystack = MyClass()
    >>> needle = 'MyClass'
    >>> inrepr(needle, haystack)
    True

    :param needle: Substring which may be within haystack.
    :param haystack: Object which is inspected for needle.
    :returns: Boolean indicating if needle is in haystack.
    """

    return hasstr(repr(haystack), needle)



def instr(
    needle: str,
    haystack: Any,  # noqa: ANN401
) -> bool:
    """
    Return the boolean indicating if needle is in haystack.

    Example
    -------
    >>> class MyClass: pass
    >>> haystack = MyClass()
    >>> needle = 'MyClass'
    >>> instr(needle, haystack)
    True

    :param needle: Substring which may be within haystack.
    :param haystack: Object which is inspected for needle.
    :returns: Boolean indicating if needle is in haystack.
    """

    return hasstr(str(haystack), needle)
