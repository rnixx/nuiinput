'''
Motion Event Dispatcher
=======================

Dispatcher for :class:`~nuiinput.motionevent.MotionEvent` instances.
'''

__all__ = ('MotionEventDispatcher', )


class MotionEventDispatcher:
    _on_motion = []
    _on_touch_down = []
    _on_touch_move = []
    _on_touch_up = []
    _on_mouse_pos = []

    @classmethod
    def on_motion(cls, callback):
        cls._on_motion.append(callback)

    @classmethod
    def on_touch_down(cls, callback):
        cls._on_touch_down.append(callback)

    @classmethod
    def on_touch_move(cls, callback):
        cls._on_touch_move.append(callback)

    @classmethod
    def on_touch_up(cls, callback):
        cls._on_touch_up.append(callback)

    @classmethod
    def on_mouse_pos(cls, callback):
        cls._on_mouse_pos.append(callback)
