# pylint: disable=W0611
'''
Providers
=========

'''

import os

from nuiinput.utils import platform as core_platform
from nuiinput.logger import logger
from nuiinput.setupconfig import USE_SDL2

import nuiinput.providers.tuio
import nuiinput.providers.mouse

platform = core_platform

if platform == 'win' or 'NUIINPUT_DOC' in os.environ:
    try:
        import nuiinput.providers.wm_touch
        import nuiinput.providers.wm_pen
    except:
        err = 'Input: WM_Touch/WM_Pen not supported by your version of Windows'
        logger.warning(err)

if platform == 'macosx' or 'NUIINPUT_DOC' in os.environ:
    try:
        import nuiinput.providers.mactouch
    except:
        err = 'Input: MacMultitouchSupport is not supported by your system'
        logger.exception(err)

if platform == 'linux' or 'NUIINPUT_DOC' in os.environ:
    try:
        import nuiinput.providers.probesysfs
    except:
        err = 'Input: ProbeSysfs is not supported by your version of linux'
        logger.exception(err)
    try:
        import nuiinput.providers.mtdev
    except:
        err = 'Input: MTDev is not supported by your version of linux'
        logger.exception(err)
    try:
        import nuiinput.providers.hidinput
    except:
        err = 'Input: HIDInput is not supported by your version of linux'
        logger.exception(err)
    try:
        import nuiinput.providers.linuxwacom
    except:
        err = 'Input: LinuxWacom is not supported by your version of linux'
        logger.exception(err)

if (platform == 'android' and not USE_SDL2) or 'NUIINPUT_DOC' in os.environ:
    try:
        import nuiinput.providers.androidjoystick
    except:
        err = 'Input: AndroidJoystick is not supported by your version ' \
              'of linux'
        logger.exception(err)

try:
    import nuiinput.providers.leapfinger  # NOQA
except:
    err = 'Input: LeapFinger is not available on your system'
    logger.exception(err)
