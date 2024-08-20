"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Optional

from ..types import BaseModel



_CRYPTS = dict[str, 'CryptParams']



class CryptParams(BaseModel, extra='forbid'):
    """
    Process and validate the core configuration parameters.

    :param phrase: Passphrases that are used in operations.
    :param data: Keyword arguments passed to Pydantic model.
        Parameter is picked up by autodoc, please ignore.
    """

    phrase: str



class CryptsParams(BaseModel, extra='forbid'):
    """
    Process and validate the core configuration parameters.

    :param phrases: Passphrases that are used in operations.
    """

    phrases: _CRYPTS


    def __init__(
        self,
        phrases: Optional[_CRYPTS] = None,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        if phrases is None:
            phrases = {}

        super().__init__(
            phrases=phrases)
