Enasis Network Common Library
=============================

Configuration Container
-----------------------

.. autoclass:: encommon.config.Config
   :members:
   :show-inheritance:
   :noindex:

.. autopydantic_model:: encommon.config.ConfigParams
   :members:
   :show-inheritance:
   :noindex:

Parameters Container
--------------------

.. autopydantic_model:: encommon.config.Params
   :members:
   :show-inheritance:
   :noindex:

Configuration Content
---------------------

.. autoclass:: encommon.config.ConfigFile
   :members:
   :show-inheritance:
   :noindex:

.. autoclass:: encommon.config.ConfigFiles
   :members:
   :show-inheritance:
   :noindex:

.. autoclass:: encommon.config.ConfigPath
   :members:
   :show-inheritance:
   :noindex:

.. autoclass:: encommon.config.ConfigPaths
   :members:
   :show-inheritance:
   :noindex:

Configuration Logger
--------------------

.. autoclass:: encommon.config.Logger
   :members:
   :show-inheritance:
   :noindex:

.. autopydantic_model:: encommon.config.LoggerParams
   :members:
   :show-inheritance:
   :noindex:

.. autoclass:: encommon.config.Message
   :members:
   :show-inheritance:
   :noindex:

Configuration Utilities
-----------------------

.. autofunction:: encommon.config.config_load
   :noindex:

.. autofunction:: encommon.config.config_path
   :noindex:

.. autofunction:: encommon.config.config_paths
   :noindex:

Encryption and Decryption
-------------------------

.. autoclass:: encommon.crypts.Crypts
   :members:
   :show-inheritance:
   :noindex:

.. autopydantic_model:: encommon.crypts.CryptsParams
   :members:
   :show-inheritance:
   :noindex:

Hashing Algorithms
------------------

.. autoclass:: encommon.crypts.Hashes
   :members:
   :show-inheritance:
   :noindex:

Color Formatting
----------------

.. autoclass:: encommon.colors.Color
   :members:
   :show-inheritance:
   :noindex:

Jinja2 Templating
-----------------

.. autoclass:: encommon.parse.Jinja2
   :members:
   :show-inheritance:
   :noindex:

Network Addresses
-----------------

.. autoclass:: encommon.parse.Network
   :members:
   :show-inheritance:
   :noindex:

.. autofunction:: encommon.parse.insubnet_ip
   :noindex:

.. autofunction:: encommon.parse.isvalid_ip
   :noindex:

Advanced Time Structures
------------------------

.. autoclass:: encommon.times.Time
   :members:
   :show-inheritance:
   :noindex:

.. autoclass:: encommon.times.Duration
   :members:
   :show-inheritance:
   :noindex:

.. autoclass:: encommon.times.Timer
   :members:
   :show-inheritance:
   :noindex:

.. autopydantic_model:: encommon.times.TimerParams
   :members:
   :show-inheritance:
   :noindex:

.. autoclass:: encommon.times.Timers
   :members:
   :show-inheritance:
   :noindex:

.. autopydantic_model:: encommon.times.TimersParams
   :members:
   :show-inheritance:
   :noindex:

.. autoclass:: encommon.times.Window
   :members:
   :show-inheritance:
   :noindex:

.. autopydantic_model:: encommon.times.WindowParams
   :members:
   :show-inheritance:
   :noindex:

.. autoclass:: encommon.times.Windows
   :members:
   :show-inheritance:
   :noindex:

.. autopydantic_model:: encommon.times.WindowsParams
   :members:
   :show-inheritance:
   :noindex:

Datetime and Helpers
--------------------

.. autofunction:: encommon.times.parse_time
   :noindex:

.. autofunction:: encommon.times.shift_time
   :noindex:

.. autofunction:: encommon.times.since_time
   :noindex:

.. autofunction:: encommon.times.string_time
   :noindex:

.. autofunction:: encommon.times.findtz
   :noindex:

.. autofunction:: encommon.times.unitime
   :noindex:

Unique Python Types
-------------------

.. autodata:: encommon.types.Empty
   :noindex:

Python Type Utilities
---------------------

.. autofunction:: encommon.types.merge_dicts
   :noindex:

.. autofunction:: encommon.types.sort_dict
   :noindex:

.. autofunction:: encommon.types.dedup_list
   :noindex:

.. autofunction:: encommon.types.fuzzy_list
   :noindex:

.. autofunction:: encommon.types.strplwr
   :noindex:

.. autofunction:: encommon.types.hasstr
   :noindex:

.. autofunction:: encommon.types.inrepr
   :noindex:

.. autofunction:: encommon.types.instr
   :noindex:

.. autofunction:: encommon.types.clsname
   :noindex:

.. autofunction:: encommon.types.funcname
   :noindex:

.. autofunction:: encommon.types.lattrs
   :noindex:

.. autofunction:: encommon.types.inlist
   :noindex:

.. autofunction:: encommon.types.rplstr
   :noindex:

Python Notation Helpers
-----------------------

.. autofunction:: encommon.types.getate
   :noindex:

.. autofunction:: encommon.types.setate
   :noindex:

.. autofunction:: encommon.types.delate
   :noindex:

.. autofunction:: encommon.types.impate
   :noindex:

.. autofunction:: encommon.types.expate
   :noindex:

Colorized Standard Output
-------------------------

.. autofunction:: encommon.utils.array_ansi
   :noindex:

.. autofunction:: encommon.utils.kvpair_ansi
   :noindex:

.. autofunction:: encommon.utils.make_ansi
   :noindex:

.. autofunction:: encommon.utils.print_ansi
   :noindex:

.. autofunction:: encommon.utils.strip_ansi
   :noindex:

Test Sample Utilities
---------------------

.. autofunction:: encommon.utils.load_sample
   :noindex:

.. autofunction:: encommon.utils.prep_sample
   :noindex:

.. autofunction:: encommon.utils.read_sample
   :noindex:

.. autofunction:: encommon.utils.rvrt_sample
   :noindex:

Matching Expressions
--------------------

.. autofunction:: encommon.utils.fuzz_match
   :noindex:

.. autofunction:: encommon.utils.rgxp_match
   :noindex:

File System and Paths
---------------------

.. autofunction:: encommon.utils.read_text
   :noindex:

.. autofunction:: encommon.utils.save_text
   :noindex:

.. autofunction:: encommon.utils.append_text
   :noindex:

.. autofunction:: encommon.utils.resolve_path
   :noindex:

.. autofunction:: encommon.utils.resolve_paths
   :noindex:

.. autofunction:: encommon.utils.stats_path
   :noindex:

WebKit Content
--------------

.. autoclass:: encommon.webkit.Content
   :noindex:

WebKit JavaScript
-----------------

.. js:autofunction:: colordiv

.. js:autofunction:: datagrid

.. js:autofunction:: datestamp

.. js:autofunction:: duration

.. js:autofunction:: assert

.. js:autofunction:: whenready

.. js:autofunction:: isnull

.. js:autofunction:: isempty

.. js:autofunction:: isbool

.. js:autofunction:: isstr

.. js:autofunction:: isnum

.. js:autofunction:: isquery

.. js:autofunction:: isnode

.. js:autofunction:: isnodes

.. js:autofunction:: istime

.. js:autofunction:: islist

.. js:autofunction:: isdict

.. js:autofunction:: istrue

.. js:autofunction:: isfalse

.. js:autofunction:: loads

.. js:autofunction:: dumps

.. js:autofunction:: svgicon

.. js:autofunction:: message

.. js:autofunction:: moderate

.. js:autofunction:: numeric

.. js:autofunction:: numeric_count

.. js:autofunction:: numeric_bytes

.. js:autofunction:: numeric_ftemp

.. js:autofunction:: numeric_cftemp

.. js:autofunction:: statate

.. js:autofunction:: tagues
