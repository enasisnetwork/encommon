"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from re import compile
from re import match as re_match
from typing import Any
from uuid import UUID



VALID_UUID = compile(
    '^[0-9a-fA-F]{8}-'
    '([0-9a-fA-F]{4}-){3}'
    '[0-9a-fA-F]{12}$')



def isvalid_uuid(
    value: Any,  # noqa: ANN401
) -> bool:
    """
    Return the boolean indicating whether the value is valid.

    :param value: Value that will be validated by function.
    :returns: Boolean indicating whether the value is valid.
    """

    if isinstance(value, UUID):
        return True

    value = str(value)

    match = re_match(
        VALID_UUID, value)

    return match is not None
