"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path
from typing import Any

from pytest import fixture
from pytest import raises

from ..params import WindowParams
from ..params import WindowsParams
from ..windows import Windows
from ...types import inrepr
from ...types import instr



@fixture
def windows(
    tmp_path: Path,
) -> Windows:
    """
    Construct the instance for use in the downstream tests.

    :param tmp_path: pytest object for temporal filesystem.
    :returns: Newly constructed instance of related class.
    """

    source: dict[str, Any] = {
        'one': WindowParams(
            window='* * * * *',
            start=310,
            stop=610,
            delay=10),
        'two': WindowParams(
            window='* * * * *',
            start=300,
            stop=620,
            delay=10)}

    params = WindowsParams(
        windows=source)

    windows = Windows(
        params,
        start=310,
        stop=610,
        file=f'{tmp_path}/cache.db')

    sqlite = windows.sqlite

    sqlite.execute(
        """
        insert into windows
        ("group", "unique",
         "last", "next",
         "update")
        values (
         "default", "two",
         "1970-01-01T00:06:00Z",
         "1970-01-01T00:07:00Z",
         "1970-01-01T01:00:00Z")
        """)  # noqa: LIT003

    sqlite.commit()

    sqlite.execute(
        """
        insert into windows
        ("group", "unique",
         "last", "next",
         "update")
        values (
         "default", "tre",
         "1970-01-01T00:06:00Z",
         "1970-01-01T00:07:00Z",
         "1970-01-01T01:00:00Z")
        """)  # noqa: LIT003

    sqlite.commit()

    windows.load_children()

    return windows



def test_Windows(
    windows: 'Windows',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param windows: Primary class instance for window object.
    """


    attrs = list(windows.__dict__)

    assert attrs == [
        '_Windows__params',
        '_Windows__start',
        '_Windows__stop',
        '_Windows__sqlite',
        '_Windows__file',
        '_Windows__table',
        '_Windows__group',
        '_Windows__windows']


    assert inrepr(
        'windows.Windows object',
        windows)

    assert hash(windows) > 0

    assert instr(
        'windows.Windows object',
        windows)


    assert windows.params is not None

    assert windows.start == (
        '1970-01-01T00:05:10Z')

    assert windows.stop == (
        '1970-01-01T00:10:10Z')

    assert windows.sqlite is not None

    assert windows.file[-8:] == 'cache.db'

    assert windows.table == 'windows'

    assert windows.group == 'default'

    assert len(windows.children) == 2


    window = windows.children['one']

    assert window.next == (
        '1970-01-01T00:06:00Z')

    assert window.last == (
        '1970-01-01T00:05:00Z')


    window = windows.children['two']

    assert window.next == (
        '1970-01-01T00:08:00Z')

    assert window.last == (
        '1970-01-01T00:07:00Z')



def test_Windows_cover(
    windows: 'Windows',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param windows: Primary class instance for window object.
    """


    assert windows.ready('one')

    assert windows.ready('two')


    windows.update('two', '+1h')

    assert not windows.ready('two')

    windows.load_children()

    assert windows.ready('two')


    windows.update('two', '+1h')

    assert not windows.ready('two')

    windows.save_children()
    windows.load_children()

    assert not windows.ready('two')


    params = WindowParams(
        window='* * * * *',
        start=310,
        stop=610,
        delay=10)

    windows.create('fur', params)

    assert windows.ready('fur')

    windows.delete('fur')



def test_Windows_raises(
    windows: Windows,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param windows: Primary class instance for window object.
    """


    _raises = raises(ValueError)

    with _raises as reason:
        windows.ready('dne')

    _reason = str(reason.value)

    assert _reason == 'unique'


    _raises = raises(ValueError)

    params = WindowParams(
        window='* * * * *')

    with _raises as reason:
        windows.create('one', params)

    _reason = str(reason.value)

    assert _reason == 'unique'


    _raises = raises(ValueError)

    with _raises as reason:
        windows.update('dne', 'now')

    _reason = str(reason.value)

    assert _reason == 'unique'


    _raises = raises(ValueError)

    with _raises as reason:
        windows.delete('dne')

    _reason = str(reason.value)

    assert _reason == 'unique'
