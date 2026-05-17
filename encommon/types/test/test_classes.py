"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING

from ..classes import clsname
from ..classes import lattrs

if TYPE_CHECKING:
    from ...config.config import Config



def test_clsname(
    config: 'Config',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param config: Primary class instance for configuration.
    """

    assert clsname(config) == 'Config'



def test_lattrs(
    config: 'Config',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param config: Primary class instance for configuration.
    """

    attrs = lattrs(config)

    assert attrs == [
        '_Config__valid',
        '_Config__files',
        '_Config__cargs',
        '_Config__sargs',
        '_Config__params',
        '_Config__paths',
        '_Config__logger',
        '_Config__crypts',
        '_Config__jinja2']
