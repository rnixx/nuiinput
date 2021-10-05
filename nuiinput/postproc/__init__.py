'''
Input Postprocessing
====================

'''

__all__ = ('nuiinput_postproc_modules', )

import os
from nuiinput.postproc.doubletap import InputPostprocDoubleTap
from nuiinput.postproc.tripletap import InputPostprocTripleTap
from nuiinput.postproc.ignorelist import InputPostprocIgnoreList
from nuiinput.postproc.retaintouch import InputPostprocRetainTouch
from nuiinput.postproc.dejitter import InputPostprocDejitter
from nuiinput.postproc.calibration import InputPostprocCalibration

# Mapping of ID to module
nuiinput_postproc_modules = {}

# Don't go further if we generate documentation
if 'NUIINPUT_DOC' not in os.environ:
    nuiinput_postproc_modules['calibration'] = InputPostprocCalibration()
    nuiinput_postproc_modules['retaintouch'] = InputPostprocRetainTouch()
    nuiinput_postproc_modules['ignorelist'] = InputPostprocIgnoreList()
    nuiinput_postproc_modules['doubletap'] = InputPostprocDoubleTap()
    nuiinput_postproc_modules['tripletap'] = InputPostprocTripleTap()
    nuiinput_postproc_modules['dejitter'] = InputPostprocDejitter()
