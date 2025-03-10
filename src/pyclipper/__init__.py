"""
Python bindings for the C++ translation of the Angus Johnson's Clipper library
(version 6.4.2): http://www.angusj.com/delphi/clipper.php

This modified version of pyclipper requires all points to have 3 coordinates (X, Y, Z).
The Z coordinate is not used for geometric clipping operations but is carried 
through the clipping process and can be used to store vertex property data.

All points must be provided as sequences of 3 values: [X, Y, Z]
"""

from ._pyclipper import *

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0.0.0+unknown"
