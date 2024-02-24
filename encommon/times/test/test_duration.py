"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from ..duration import Duration



def test_Duration() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    duration = Duration(60)

    attrs = list(duration.__dict__)

    assert attrs == [
        '_Duration__source',
        '_Duration__smart']


    assert repr(duration) == (
        'Duration(60.0, True)')
    assert isinstance(hash(duration), int)
    assert str(duration) == '1m'


    assert int(duration) == 60
    assert float(duration) == 60

    assert duration + 1 == 61
    assert duration + duration == 120
    assert duration - 1 == 59
    assert duration - duration == 0

    assert duration == duration
    assert duration != Duration(61)
    assert duration != 'invalid'

    assert duration > Duration(59)
    assert duration >= Duration(60)
    assert duration < Duration(61)
    assert duration <= Duration(60)


    assert duration.source == 60
    assert duration.smart is True

    assert duration.compact == '1m'
    assert duration.verbose == '1 minute'



def test_Duration_cover() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    second = 60
    hour = second * 60
    day = hour * 24
    week = day * 7
    month = day * 30
    quarter = day * 90
    year = day * 365


    expects = {

        year: ('1y', '1 year'),
        year + 1: ('1y', '1 year'),
        year - 1: (
            '12mon4d23h59m',
            '12 months, 4 days'),

        quarter: ('3mon', '3 months'),
        quarter + 1: ('3mon', '3 months'),
        quarter - 1: (
            '2mon4w1d23h59m',
            '2 months, 4 weeks'),

        month: ('1mon', '1 month'),
        month + 1: ('1mon', '1 month'),
        month - 1: (
            '4w1d23h59m',
            '4 weeks, 1 day'),

        week: ('1w', '1 week'),
        week + 1: ('1w', '1 week'),
        week - 1: (
            '6d23h59m',
            '6 days, 23 hours'),

        day: ('1d', '1 day'),
        day + 1: ('1d', '1 day'),
        day - 1: (
            '23h59m',
            '23 hours, 59 minutes'),

        hour: ('1h', '1 hour'),
        hour + 1: ('1h', '1 hour'),
        hour - 1: ('59m', '59 minutes'),

        second: ('1m', '1 minute'),
        second + 1: ('1m', '1 minute'),
        second - 1: ('59s', 'just now')}


    for source, expect in expects.items():

        duration = Duration(source)
        assert duration.compact == expect[0]

        duration = Duration(source)
        verbose = ', '.join(
            duration.verbose.split(', ')[:2])

        assert verbose == expect[1]
