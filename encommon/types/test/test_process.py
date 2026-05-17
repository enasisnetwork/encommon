"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Any

from ..empty import Empty
from ..empty import EmptyType
from ..notate import expate
from ..process import process
from ..process import prune



class CustomEmpty(EmptyType):
    """
    Useful for representing empty or absent value with typing.
    """



def test_prune() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    source: Any


    # TEST remove empty values

    source = expate({
        'a': None,
        'b/c': [None, [Empty]],
        'd': CustomEmpty(),
        'e': CustomEmpty})

    result = prune(source)

    assert result == {}



def test_process() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    source: Any
    expect: Any


    # TEST remove empty values

    source = expate({
        'a': None,
        'b/c': [None, [Empty]],
        'd': CustomEmpty(),
        'e': CustomEmpty})

    result = process(
        source=source,
        prune_empty=True)

    assert result == {}


    # TEST process the values

    source = [1, '2', [3, '4']]
    expect = [1, 2, [3, 4]]

    result = process(
        source,
        processor=lambda _, v: int(v))

    assert result == expect


    # TEST process the values

    source = {
        'a': 1,
        'b': '2',
        'c': {'d': '3'}}

    expect = {
        'a': 1,
        'b': 2,
        'c': {'d': 3}}

    result = process(
        source,
        processor=lambda _, v: int(v))

    assert result == expect




def test_process_types() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    source: Any
    expect: Any


    # TEST block and allow types

    source = {
        'a': ['1', 2],
        'b': {'c': '1', 'd': 2}}

    block_types = [str]
    allow_types = [int]

    expect = {
        'a': [2],
        'b': {'d': 2}}

    result = process(
        source=source,
        block_types=block_types,
        paranoid=True)

    assert result == expect

    result = process(
        source=source,
        allow_types=allow_types,
        paranoid=True)

    assert result == expect



def test_process_values() -> None:  # noqa: CFQ001
    """
    Perform various tests associated with relevant routines.
    """

    source: Any
    block_values: Any
    allow_values: Any
    expect: Any


    # TEST deduplicate the lists

    source = expate({
        'a/b': [1, 1],
        'c': [1, 1, 2]})

    expect = {
        'a': {'b': [1]},
        'c': [1, 2]}

    result = process(
        source=source,
        dedup_values=True,
        paranoid=True)

    assert result == expect


    # TEST block and allow values

    source = [1, '2', None, 3]

    block_values = [1, '2']
    allow_values = [None, 3]

    expect = [None, 3]

    result = process(
        source=source,
        block_values=block_values,
        paranoid=True)

    assert result == expect

    result = process(
        source=source,
        allow_values=allow_values,
        paranoid=True)

    assert result == expect


    # TEST block and allow values

    source = [1, '2', None, 3]

    block_values = '^None$'
    allow_values = r'^\d+$'

    expect = [1, '2', 3]

    result = process(
        source=source,
        block_values=block_values,
        paranoid=True)

    assert result == expect

    result = process(
        source=source,
        allow_values=allow_values,
        paranoid=True)

    assert result == expect


    # TEST block and allow values

    source = [1, '2', None, 3]

    block_values = r'^\d+$'
    allow_values = 'N*ne'

    expect = [None]

    result = process(
        source=source,
        block_values=block_values,
        paranoid=True,
        match_method='rematch')

    assert result == expect

    result = process(
        source=source,
        allow_values=allow_values,
        paranoid=True,
        match_method='fnmatch')

    assert result == expect


    # TEST block and allow values

    source = {
        'a': 1,
        'b': '2',
        'c': None,
        'd': 3}

    block_values = [1, '2']
    allow_values = [None, 3]
    expect = {'c': None, 'd': 3}

    result = process(
        source=source,
        block_values=block_values,
        paranoid=True)

    assert result == expect

    result = process(
        source=source,
        allow_values=allow_values,
        paranoid=True)

    assert result == expect


    # TEST block and allow values

    source = {
        'a': 1,
        'b': '2',
        'c': None,
        'd': 3}

    block_values = '^None$'
    allow_values = r'^\d+$'

    expect = {
        'a': 1,
        'b': '2',
        'd': 3}

    result = process(
        source=source,
        block_values=block_values,
        paranoid=True)

    assert result == expect

    result = process(
        source=source,
        allow_values=allow_values,
        paranoid=True)

    assert result == expect


    # TEST block and allow values

    source = {
        'a': [1, 2],
        'b': {'c': 1, 'd': 2}}

    block_values = '^2$'
    allow_values = '^1$'

    expect = {
        'a': [1],
        'b': {'c': 1}}

    result = process(
        source=source,
        block_values=block_values,
        paranoid=True)

    assert result == expect

    result = process(
        source=source,
        allow_values=allow_values,
        paranoid=True)

    assert result == expect



def test_process_keys() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    source: Any
    block_keys: Any
    allow_keys: Any
    expect: Any


    # TEST block and allow values

    source = {
        'a': 1,
        'b': '2',
        'c': None,
        'd': 3}

    block_keys = ['a', 'b']
    allow_keys = ['c', 'd']
    expect = {'c': None, 'd': 3}

    result = process(
        source=source,
        block_keys=block_keys,
        paranoid=True)

    assert result == expect

    result = process(
        source=source,
        allow_keys=allow_keys,
        paranoid=True)

    assert result == expect


    # TEST block and allow values

    source = {
        'a': 1,
        'b': '2',
        'c': None,
        'd': 3}

    block_keys = '^c$'
    allow_keys = '[abd]'

    expect = {
        'a': 1,
        'b': '2',
        'd': 3}

    result = process(
        source=source,
        block_keys=block_keys,
        paranoid=True)

    assert result == expect

    result = process(
        source=source,
        allow_keys=allow_keys,
        paranoid=True)

    assert result == expect
