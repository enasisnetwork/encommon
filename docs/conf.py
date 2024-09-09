"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""
# pylint: disable=import-error



from os import path as os_path
from sys import path as sys_path

sys_path.insert(0, os_path.abspath('../'))

from encommon import VERSION  # noqa: E402



project = 'encommon'
copyright = '2024, Enasis Network'
author = 'Enasis Network'
nitpicky = True
version = VERSION

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinxcontrib.autodoc_pydantic']

html_theme = 'sphinx_rtd_theme'

always_document_param_types = True

intersphinx_mapping = {
    'pydantic': ('https://docs.pydantic.dev/latest', None),
    'pytest': ('https://docs.pytest.org/latest', None),
    'python': ('https://docs.python.org/3', None),
    'sqlalchemy': ('https://docs.sqlalchemy.org/en/20', None)}

nitpick_ignore = [

    # Seems to be an issue using Pydantic
    ('py:class', 'Field'),
    ('py:class', 'FieldInfo'),
    ('py:class', 'Ge'),
    ('py:class', 'Le'),
    ('py:class', 'MinLen'),
    ('py:class', 'NoneType'),

    # Seems to be an issue using SQLAlchemy
    ('py:class', 'MetaData'),
    ('py:class', '_RegistryType'),
    ('py:class', '_orm.registry'),
    ('py:class', '_orm.Mapper'),
    ('py:class', '_schema.MetaData'),
    ('py:class', '_schema.Table'),

    # Not sure what causes these warnings
    ('py:class', 'DataclassInstance'),
    ('py:class', 'PARSABLE'),
    ('py:class', 'PATHABLE'),
    ('py:class', 'REPLACE')]
