"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from datetime import datetime
from datetime import tzinfo



def snap(
    dttm: datetime,
    instruction: str,
) -> datetime: ...



def snap_tz(
    dttm: datetime,
    instruction: str,
    timezone: tzinfo,
) -> datetime: ...
