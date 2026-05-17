"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from copy import deepcopy
from fnmatch import fnmatch
from inspect import isclass
from re import match as re_match
from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import TypeVar

from .empty import Empty
from .empty import EmptyType
from .lists import dedup_list



ProcessSource = TypeVar(
    'ProcessSource',
    bound=dict[Any, Any] | list[Any])



def prune(
    source: ProcessSource,
    *,
    recurse: bool = True,
    paranoid: bool = False,
) -> ProcessSource:
    """
    Process the provided source value removing empty values.

    .. warning::
       This function will update the ``source`` reference.

    :param source: Supported object processed in operation.
    :param recurse: Process the provided source recursively.
    :param paranoid: Perform deepcopy of source value first.
    """

    return process(
        source,
        recurse=recurse,
        paranoid=paranoid,
        prune_empty=True)



def process(  # noqa: CFQ001,CFQ002,CFQ004
    source: ProcessSource,
    *,
    recurse: bool = True,
    paranoid: bool = False,
    dedup_values: bool = False,
    allow_values: Optional[list[Any] | str] = None,
    block_values: Optional[list[Any] | str] = None,
    allow_keys: Optional[list[Any] | str] = None,
    block_keys: Optional[list[Any] | str] = None,
    allow_types: Optional[list[Any] | tuple[Any, ...]] = None,
    block_types: Optional[list[Any] | tuple[Any, ...]] = None,
    match_method: Literal['rematch', 'fnmatch'] = 'rematch',
    prune_empty: bool = False,
    processor: Optional[Callable[..., Any]] = None,
) -> ProcessSource:
    """
    Process the provided iterable source updating in place.

    .. warning::
       This function will update the ``source`` reference.

    .. note::
       Parameters like ``allow_values`` accept either list
       of exact values or a single pattern string; regular
       expression or fnmatch pattern, see ``match_method``.

    Example
    -------
    >>> source = {'a': {'b': '1'}}
    >>> process(source, processor=lambda _, v: int(v))
    {'a': {'b': 1}}
    >>> source
    {'a': {'b': 1}}

    :param source: Supported object processed in operation.
    :param recurse: Process the provided source recursively.
    :param paranoid: Perform deepcopy of source value first.
    """

    from ..utils.raises import Unexpected

    if paranoid is True:
        source = deepcopy(source)


    Recurse = (list, dict)
    Iterate = (str, list, dict, tuple)


    allow_types = (
        tuple(allow_types)
        if allow_types is not None
        else None)

    block_types = (
        tuple(block_types)
        if block_types is not None
        else None)


    remove: list[str | int] = []


    def _match(
        source: Any,  # noqa: ANN401
        regexp: str,
    ) -> bool:

        source = str(source)

        if (match_method == 'rematch'
                and re_match(regexp, source)):
            return True

        elif (match_method == 'fnmatch'
                and fnmatch(source, regexp)):
            return True

        return False


    def _isempty(  # noqa: CFQ004
        value: Any,  # noqa: ANN401
    ) -> bool:

        if value is None:
            return True

        if (isinstance(value, Iterate)
                and len(value) == 0):
            return True

        if (value is Empty
                or isinstance(value, EmptyType)):
            return True

        if (isclass(value)
                and issubclass(value, EmptyType)):
            return True

        return False


    def _allowed(  # noqa: CFQ004
        target: Any,  # noqa: ANN401
        allow: Optional[list[Any] | str],
        block: Optional[list[Any] | str],
    ) -> bool:

        if allow is not None:

            if isinstance(allow, str):
                if not _match(target, allow):
                    return False

            elif target not in allow:
                return False

        if block is not None:

            if isinstance(block, str):
                if _match(target, block):
                    return False

            elif target in block:
                return False

        return True


    items = (
        source.items()
        if isinstance(source, dict)
        else enumerate(source))

    for ikey, ivalue in list(items):


        # STEP process with processor

        if (processor is not None
                and not isinstance(
                    ivalue, Recurse)):
            ivalue = processor(ikey, ivalue)
            source[ikey] = ivalue


        # STEP remove any empty values

        if (prune_empty is True
                and _isempty(ivalue)):
            remove.append(ikey)
            continue


        # STEP restrict allowed keys

        allowed = _allowed(
            ikey,
            allow_keys,
            block_keys)

        if allowed is False:
            remove.append(ikey)
            continue


        # STEP recurse when relevant

        if isinstance(ivalue, Recurse):

            if (dedup_values is True
                    and isinstance(ivalue, list)):
                dedup_list(ivalue)

            if recurse is True:
                process(
                    source=ivalue,
                    recurse=recurse,
                    dedup_values=dedup_values,
                    block_values=block_values,
                    allow_values=allow_values,
                    block_keys=block_keys,
                    allow_keys=allow_keys,
                    block_types=block_types,
                    allow_types=allow_types,
                    match_method=match_method,
                    prune_empty=prune_empty,
                    processor=processor)

            # STEP remove if empty value

            if (prune_empty is True
                    and _isempty(ivalue)):
                remove.append(ikey)

            continue


        # STEP restrict allowed types

        if (allow_types is not None
                and not isinstance(
                    ivalue, allow_types)):
            remove.append(ikey)
            continue

        if (block_types is not None
                and isinstance(
                    ivalue, block_types)):
            remove.append(ikey)
            continue


        # STEP restrict allowed values

        allowed = _allowed(
            ivalue,
            allow_values,
            block_values)

        if allowed is False:
            remove.append(ikey)
            continue


    # STEP remove collected keys

    keys = (
        sorted(remove, reverse=True)
        if isinstance(source, list)
        else remove)

    for key in keys:

        if isinstance(source, list):
            assert isinstance(key, int)
            del source[key]
            continue

        if isinstance(source, dict):
            assert isinstance(key, str)
            del source[key]
            continue

        raise Unexpected


    return source
