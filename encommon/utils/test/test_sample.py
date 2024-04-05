"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path

from ..sample import load_sample
from ..sample import prep_sample
from ... import ENPYRWS
from ... import PROJECT



def test_prep_sample() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    assert prep_sample((1, '2')) == [1, '2']



def test_load_sample(
    tmp_path: Path,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param tmp_path: pytest object for temporal filesystem.
    """

    prefix = 'encommon_sample'

    source = {
        'list': ['bar', 'baz'],
        'tuple': (1, 2),
        'project': PROJECT,
        'other': '/pat/h'}

    expect = {
        'list': ['bar', 'baz'],
        'tuple': [1, 2],
        'project': f'_/{prefix}/PROJECT/_',
        'other': f'_/{prefix}/tmp_path/_'}


    replaces = {
        'PROJECT': str(PROJECT),
        'tmp_path': '/pat/h'}


    sample_path = (
        f'{tmp_path}/samples.json')

    sample = load_sample(
        path=sample_path,
        update=ENPYRWS,
        content=source,
        replace=replaces)

    assert sample == expect


    source |= {'list': [1, 3, 2]}
    expect |= {'list': [1, 3, 2]}

    sample = load_sample(
        path=sample_path,
        content=source,
        update=True,
        replace=replaces)

    assert sample == expect
