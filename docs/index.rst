Configuration Container
=======================

.. autoclass:: encommon.config.Config
   :members:
   :show-inheritance:
   :noindex:

.. autopydantic_model:: encommon.config.ConfigParams
   :members:
   :show-inheritance:
   :noindex:

Parameters Container
====================

.. autopydantic_model:: encommon.config.Params
   :members:
   :show-inheritance:
   :noindex:

Configuration Content
=====================

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
====================

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
=======================

.. autofunction:: encommon.config.config_load
   :noindex:

.. autofunction:: encommon.config.config_path
   :noindex:

.. autofunction:: encommon.config.config_paths
   :noindex:

Encryption and Decryption
=========================

.. autoclass:: encommon.crypts.Crypts
   :members:
   :show-inheritance:
   :noindex:

.. autopydantic_model:: encommon.crypts.CryptsParams
   :members:
   :show-inheritance:
   :noindex:

Hashing Algorithms
==================

.. autoclass:: encommon.crypts.Hashes
   :members:
   :show-inheritance:
   :noindex:

Advanced Time Structures
========================

.. autoclass:: encommon.times.Times
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
====================
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

Unique Python Types
===================

.. autodata:: encommon.types.Empty
   :noindex:

Python Type Utilities
=====================

.. autofunction:: encommon.types.merge_dicts
   :noindex:

.. autofunction:: encommon.types.sort_dict
   :noindex:

.. autofunction:: encommon.types.striplower
   :noindex:

.. autofunction:: encommon.types.hasstr
   :noindex:

.. autofunction:: encommon.types.inrepr
   :noindex:

.. autofunction:: encommon.types.instr
   :noindex:

Python Notation Helpers
=======================

.. autofunction:: encommon.types.getate
   :noindex:

.. autofunction:: encommon.types.setate
   :noindex:

.. autofunction:: encommon.types.delate
   :noindex:

Colorized Standard Output
=========================

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
=====================

.. autofunction:: encommon.utils.load_sample
   :noindex:

.. autofunction:: encommon.utils.prep_sample
   :noindex:

Matching Expressions
====================

.. autofunction:: encommon.utils.fuzz_match
   :noindex:

.. autofunction:: encommon.utils.rgxp_match
   :noindex:

File System and Paths
=====================

.. autofunction:: encommon.utils.read_text
   :noindex:

.. autofunction:: encommon.utils.save_text
   :noindex:

.. autofunction:: encommon.utils.resolve_path
   :noindex:

.. autofunction:: encommon.utils.resolve_paths
   :noindex:

.. autofunction:: encommon.utils.stats_path
   :noindex:
