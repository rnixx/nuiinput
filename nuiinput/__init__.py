# pylint: disable=W0611
'''
Input management
================

Our input system is wide and simple at the same time. We are currently able to
natively support :

* Windows multitouch events (pencil and finger)
* OS X touchpads
* Linux multitouch events (kernel and mtdev)
* Linux wacom drivers (pencil and finger)
* TUIO

All the input management is configurable in the Kivy :mod:`~nuiinput.config`. You
can easily use many multitouch devices in one Kivy application.

When the events have been read from the devices, they are dispatched through
a post processing module before being sent to your application. We also have
several default modules for :

* Double tap detection
* Decreasing jittering
* Decreasing the inaccuracy of touch on "bad" DIY hardware
* Ignoring regions
'''


from nuiinput.motionevent import MotionEvent
from nuiinput.postproc import nuiinput_postproc_modules
from nuiinput.provider import MotionEventProvider
from nuiinput.factory import MotionEventFactory
import nuiinput.providers  # noqa

__all__ = (
    MotionEvent.__name__,
    MotionEventProvider.__name__,
    MotionEventFactory.__name__,
    'nuiinput_postproc_modules')
