"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path
from time import sleep

from pytest import raises

from ..timers import Timers



def test_Timers() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    timers = Timers({'one': 1})

    attrs = list(timers.__dict__)

    assert attrs == [
        '_Timers__timers',
        '_Timers__sqlite',
        '_Timers__table',
        '_Timers__cached']


    assert repr(timers)[:22] == (
        '<encommon.times.timers')

    assert hash(timers) > 0

    assert str(timers)[:22] == (
        '<encommon.times.timers')


    assert timers.timers == {'one': 1}
    assert timers.cache_file is not None
    assert timers.cache_name is not None
    assert len(timers.cache_dict) == 1


    assert not timers.ready('one')
    sleep(1.1)
    assert timers.ready('one')


    timers.create('two', 2, 0)

    assert timers.ready('two')
    assert not timers.ready('two')



def test_Timers_cache(
    tmp_path: Path,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param tmp_path: pytest object for temporal filesystem.
    """

    cache_file = (
        f'{tmp_path}/timers.db')

    timers1 = Timers(
        timers={'one': 1},
        cache_file=cache_file)

    assert not timers1.ready('one')

    sleep(0.75)

    timers2 = Timers(
        timers={'one': 1},
        cache_file=cache_file)

    assert not timers1.ready('one')
    assert not timers2.ready('one')

    sleep(0.25)

    timers2.load_cache()

    assert timers1.ready('one')
    assert timers2.ready('one')



def test_Timers_raises() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    timers = Timers({'one': 1})


    _raises = raises(ValueError)

    with _raises as reason:
        timers.ready('dne')

    _reason = str(reason.value)

    assert _reason == 'unique'


    _raises = raises(ValueError)

    with _raises as reason:
        timers.update('dne')

    _reason = str(reason.value)

    assert _reason == 'unique'


    _raises = raises(ValueError)

    with _raises as reason:
        timers.create('one', 1)

    _reason = str(reason.value)

    assert _reason == 'unique'
