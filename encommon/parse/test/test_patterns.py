"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from uuid import uuid4

from ..patterns import isvalid_uuid



def test_isvalid_uuid() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    notone = 'notauuid'
    isone = uuid4()
    string = str(isone)

    assert not isvalid_uuid(notone)
    assert isvalid_uuid(isone)
    assert isvalid_uuid(string)
