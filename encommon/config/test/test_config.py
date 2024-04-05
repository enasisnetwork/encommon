"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path

from . import SAMPLES
from ..config import Config
from ..params import Params
from ... import ENPYRWS
from ... import PROJECT
from ...utils.sample import load_sample
from ...utils.sample import prep_sample



def test_Config(
    tmp_path: Path,
    config: 'Config',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param tmp_path: pytest object for temporal filesystem.
    :param config: Primary class instance for configuration.
    """


    attrs = list(config.__dict__)

    assert attrs == [
        '_Config__model',
        '_Config__files',
        '_Config__cargs',
        '_Config__params',
        '_Config__paths',
        '_Config__logger',
        '_Config__crypts']


    assert repr(config)[:23] == (
        '<encommon.config.config')

    assert hash(config) > 0

    assert str(config)[:23] == (
        '<encommon.config.config')


    assert config.files is not None
    assert config.paths is not None
    assert config.cargs is not None
    assert config.config is not None
    assert config.model is Params
    assert config.params is not None
    assert config.logger is not None
    assert config.crypts is not None


    replaces = {
        'pytemp': tmp_path,
        'PROJECT': PROJECT}

    sample_path = (
        f'{SAMPLES}/config.json')

    sample = load_sample(
        path=sample_path,
        update=ENPYRWS,
        content=config.config,
        replace=replaces)

    expect = prep_sample(
        content=config.config,
        replace=replaces)

    assert sample == expect



def test_Config_cover(
    config: 'Config',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param config: Primary class instance for configuration.
    """


    logger1 = config.logger
    logger2 = config.logger

    assert logger1 is logger2


    crypts1 = config.crypts
    crypts2 = config.crypts

    assert crypts1 is crypts2
