"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from ..common import STAMP_SIMPLE
from ..common import UNIXEPOCH
from ..common import UNIXHPOCH
from ..common import UNIXMPOCH
from ..times import Times
from ...types import inrepr
from ...types import instr
from ...types import lattrs



def test_Times() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    times = Times(
        UNIXEPOCH,
        format=STAMP_SIMPLE)


    attrs = lattrs(times)

    assert attrs == [
        '_Times__source']


    assert inrepr(
        "Times('1970-01-01T00:00",
        times)

    assert hash(times) > 0

    assert instr(
        '1970-01-01T00:00:00.000',
        times)


    assert int(times) == 0
    assert float(times) == 0.0

    assert times + 1 == Times(1)
    assert times - 1 == Times(-1)

    assert times == Times(0)
    assert times != Times(-1)
    assert times != 'invalid'

    assert times > Times(-1)
    assert times >= Times(0)
    assert times < Times(1)
    assert times <= Times(0)


    assert times.source.year == 1970

    assert times.epoch == 0.0

    assert times.spoch == 0

    assert times.mpoch == 0.0

    assert str(times.time) == '00:00:00'

    assert times.simple == UNIXEPOCH

    assert times.subsec == UNIXMPOCH

    assert times.human == UNIXHPOCH

    assert times.elapsed >= 1672531200

    assert times.since >= 1672531200

    assert times.before == (
        '1969-12-31T23:59:59.999999Z')

    assert times.after == (
        '1970-01-01T00:00:00.000001Z')

    assert times.stamp() == UNIXMPOCH

    times = times.shift('+1y')
    assert times == '1971-01-01'

    times = times.shifz('UTC-1')
    assert times == (
        '12/31/1970 23:00 -0100')



def test_Times_tzname() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    times1 = Times(
        '1970-01-01T00:00:00Z')

    times2 = times1.shifz(
        'US/Central')


    delta = times1 - times2

    assert -1 < delta < 1


    stamp1 = times1.stamp(
        tzname='US/Central')

    stamp2 = times2.stamp()

    assert stamp1 == stamp2
