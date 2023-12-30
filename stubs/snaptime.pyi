"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



import datetime



def snap(
    dttm: datetime.datetime,
    instruction: str,
) -> datetime.datetime: ...



def snap_tz(
    dttm: datetime.datetime,
    instruction: str,
    timezone: datetime.tzinfo,
) -> datetime.datetime: ...
