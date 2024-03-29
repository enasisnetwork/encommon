"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Optional

from pydantic import BaseModel

from .common import LOGLEVELS
from ..crypts.params import CryptsParams



class ConfigParams(BaseModel, extra='forbid'):
    """
    Process and validate the common configuration parameters.

    :param paths: Complete or relative path to config paths.
    :param data: Keyword arguments passed to Pydantic model.
        This parameter is picked up by autodoc, please ignore.
    """

    paths: Optional[list[str]] = None



class LoggerParams(BaseModel, extra='forbid'):
    """
    Process and validate the common configuration parameters.

    :param stdo_level: Minimum log message severity level.
    :param file_level: Minimum log message severity level.
    :param file_path: Enables writing to the filesystem path.
    :param data: Keyword arguments passed to Pydantic model.
        This parameter is picked up by autodoc, please ignore.
    """

    stdo_level: Optional[LOGLEVELS] = None
    file_level: Optional[LOGLEVELS] = None
    file_path: Optional[str] = None



class Params(BaseModel, extra='forbid'):
    """
    Process and validate the common configuration parameters.

    :param enconfig: Configuration for the `.Config` object.
    :param enlogger: Configuration for the `.Logger` object.
    :param encrypts: Configuration for the `.Crypts` object.
    :param data: Keyword arguments passed to Pydantic model.
        This parameter is picked up by autodoc, please ignore.
    """

    enconfig: Optional[ConfigParams] = None
    enlogger: Optional[LoggerParams] = None
    encrypts: Optional[CryptsParams] = None
