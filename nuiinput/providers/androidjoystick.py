# pylint: disable=W0611
'''
Android Joystick Input Provider
===============================

This module is based on the PyGame JoyStick Input Provider. For more
information, please refer to
`<http://www.pygame.org/docs/ref/joystick.html>`_


'''
__all__ = ('AndroidMotionEventProvider', )

import os

try:
    import android  # NOQA
except ImportError:
    if 'NUIINPUT_DOC' not in os.environ:
        raise Exception('android lib not found.')

from nuiinput.logger import logger
from nuiinput.provider import MotionEventProvider
from nuiinput.factory import MotionEventFactory
from nuiinput.shape import ShapeRect
from nuiinput.motionevent import MotionEvent
if 'NUIINPUT_DOC' not in os.environ:
    import pygame.joystick


class AndroidMotionEvent(MotionEvent):

    def depack(self, args):
        self.is_touch = True
        self.profile = ['pos', 'pressure', 'shape']
        self.sx, self.sy, self.pressure, radius = args
        self.shape = ShapeRect()
        self.shape.width = radius
        self.shape.height = radius
        super(AndroidMotionEvent, self).depack(args)


class AndroidMotionEventProvider(MotionEventProvider):

    def __init__(self, device, args):
        super(AndroidMotionEventProvider, self).__init__(device, args)
        self.joysticks = []
        self.touches = {}
        self.uid = 0
        self.window = None

    def create_joystick(self, index):
        logger.info('Android: create joystick <%d>' % index)
        js = pygame.joystick.Joystick(index)
        js.init()
        if js.get_numbuttons() == 0:
            logger.info('Android: discard joystick <%d> cause no button' %
                        index)
            return
        self.joysticks.append(js)

    def start(self):
        pygame.joystick.init()
        logger.info('Android: found %d joystick' % pygame.joystick.get_count())
        for i in range(pygame.joystick.get_count()):
            self.create_joystick(i)

    def stop(self):
        self.joysticks = []

    def update(self, dispatch_fn):
        if not self.window:
            from nuiinput.core.window import Window
            self.window = Window
        w, h = self.window.system_size
        touches = self.touches
        for joy in self.joysticks:
            jid = joy.get_id()
            pressed = joy.get_button(0)
            if pressed or jid in touches:
                x = joy.get_axis(0) * 32768. / w
                y = 1. - (joy.get_axis(1) * 32768. / h)

                # python for android do * 1000.
                pressure = joy.get_axis(2) / 1000.
                radius = joy.get_axis(3) / 1000.

                # new touch ?
                if pressed and jid not in touches:
                    self.uid += 1
                    touch = AndroidMotionEvent(self.device, self.uid,
                                            [x, y, pressure, radius])
                    touches[jid] = touch
                    dispatch_fn('begin', touch)
                # update touch
                elif pressed:
                    touch = touches[jid]
                    # avoid same touch position
                    if (touch.sx == x and touch.sy == y and
                            touch.pressure == pressure):
                        continue
                    touch.move([x, y, pressure, radius])
                    dispatch_fn('update', touch)
                # disappear
                elif not pressed and jid in touches:
                    touch = touches[jid]
                    touch.move([x, y, pressure, radius])
                    touch.update_time_end()
                    dispatch_fn('end', touch)
                    touches.pop(jid)


MotionEventFactory.register('android', AndroidMotionEventProvider)
