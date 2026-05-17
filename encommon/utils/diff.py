"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from difflib import unified_diff
from typing import Optional

from .match import rgxp_match
from .stdout import strip_ansi



def prep_diff(
    string1: str,
    string2: str,
    *,
    paths: Optional[tuple[str, str]] = None,
    ignore: Optional[list[str]] = None,
    ordered: bool = False,
    colors: bool = True,
) -> tuple[str, ...]:
    """
    Compare the two strings between each other line by line.

    :param string1: String that is used with the comparison.
    :param string2: String that is used with the comparison.
    :param paths: Optional paths related to the strings.
    :param ignore: Lines are ignored by regular expression.
    :param ordered: Determines whether the lines are sorted.
    :param colors: Determine whether console ANSI coloring.
    :returns: Lines output from diff comparison operation.
    """

    returned: list[str] = []

    _lines1 = string1.splitlines()
    _lines2 = string2.splitlines()

    if ignore is not None:

        _ignore1 = [
            x for x in _lines1
            if rgxp_match(x, ignore)]

        _lines1 = [
            x for x in _lines1
            if x not in _ignore1]

        _ignore2 = [
            x for x in _lines2
            if rgxp_match(x, ignore)]

        _lines2 = [
            x for x in _lines2
            if x not in _ignore2]

    if ordered is True:
        _lines1 = sorted(_lines1)
        _lines2 = sorted(_lines2)


    diff = unified_diff(
        _lines1, _lines2)

    for line in diff:

        string = line
        strip = line.strip()

        if (line.startswith('+')
                and strip == '+++'):

            _paths = (
                f' {paths[1]}'
                if paths is not None
                else '')

            string = (
                '\033[0;92m'
                f'{string.rstrip()}'
                f'{_paths}'
                '\033[0m')

        elif (line.startswith('+')
                and strip != '+++'):

            string = (
                '\033[0;92m'
                f'{line}'
                '\033[0m')

        elif (line.startswith('-')
                and strip == '---'):

            _paths = (
                f' {paths[0]}'
                if paths is not None
                else '')

            string = (
                '\033[0;91m'
                f'{string.rstrip()}'
                f'{_paths}'
                '\033[0m')

        elif (line.startswith('-')
                and strip != '---'):

            string = (
                '\033[0;91m'
                f'{line}'
                '\033[0m')

        returned.append(
            strip_ansi(string)
            if colors is False
            else string)


    return tuple(returned)
