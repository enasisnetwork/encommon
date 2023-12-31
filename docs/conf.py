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
copyright = '2023, Enasis Network'
author = 'Enasis Network'
master_doc = 'index'
nitpicky = True
version = VERSION

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode']

html_theme = 'sphinx_rtd_theme'

always_document_param_types = True

intersphinx_mapping = {
    'pathlib': ('https://docs.python.org/3', None),
    'pytest': ('https://docs.pytest.org/latest', None),
    'python': ('https://docs.python.org/3', None)}

nitpick_ignore = [
    ('py:class', 'pydantic.main.BaseModel')]
