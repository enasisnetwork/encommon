"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from copy import deepcopy

from . import _DICT1R
from ..notate import delate
from ..notate import getate
from ..notate import setate



def test_getate() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    source = deepcopy(_DICT1R)


    value = getate(['1', 2], '1')
    assert value == 2

    value = getate((1, 2), '1')
    assert value == 2

    value = getate({'1': 2}, '1')
    assert value == 2


    path = 'recurse/dict/key'
    value = getate(source, path)

    assert value == 'd1dict'


    path = 'recurse/list/0'
    value = getate(source, path)

    assert value == 'd1list'



def test_setate() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    source = deepcopy(_DICT1R)


    value = setate([], '0', 1)
    assert value == [1]

    value = setate({}, '0', 1)
    assert value == {'0': 1}


    path = 'recurse/dict/key'
    before = getate(source, path)
    setate(source, path, 1)
    after = getate(source, path)
    assert after == 1
    assert before == 'd1dict'


    path = 'nested/0/dict/key'
    before = getate(source, path)
    setate(source, path, 1)
    after = getate(source, path)
    assert after == 1
    assert before == 'd1dict'


    path = 'recurse/list/0'
    before = getate(source, path)
    setate(source, path, 1)
    after = getate(source, path)
    assert after == 1
    assert before == 'd1list'



def test_delate() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    source = deepcopy(_DICT1R)


    path = 'recurse/dict/key'
    before = getate(source, path)
    delate(source, path)
    after = getate(source, path)
    assert after is None
    assert before == 'd1dict'


    path = 'nested/0/dict/key'
    before = getate(source, path)
    delate(source, path)
    after = getate(source, path)
    assert after is None
    assert before == 'd1dict'


    path = 'recurse/list/0'
    before = getate(source, path)
    delate(source, path)
    after = getate(source, path)
    assert after is None
    assert before == 'd1list'
