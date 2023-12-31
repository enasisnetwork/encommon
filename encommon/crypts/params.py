"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pydantic import BaseModel



class CryptsParams(BaseModel, extra='forbid'):
    """
    Process and validate the common configuration parameters.
    """

    phrases: dict[str, str]
