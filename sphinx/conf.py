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
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinxcontrib.autodoc_pydantic',
    'sphinx_js']

html_theme = 'pydata_sphinx_theme'

always_document_param_types = True

intersphinx_mapping = {
    'jinja2': ('https://jinja.palletsprojects.com/en/latest', None),
    'netaddr': ('https://netaddr.readthedocs.io/en/latest', None),
    'pydantic': ('https://docs.pydantic.dev/latest', None),
    'pytest': ('https://docs.pytest.org/latest', None),
    'python': ('https://docs.python.org/3', None),
    'sqlalchemy': ('https://docs.sqlalchemy.org/en/20', None)}

js_source_path = [
    '../encommon/webkit/scripts']
