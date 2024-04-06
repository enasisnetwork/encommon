"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from ..strings import strplwr



def test_strplwr() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    assert strplwr(' Foo ') == 'foo'
