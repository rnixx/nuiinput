NUI Input
=========

This package provides connecting to several input sources, most notably touch
screens, and receive input data as motion events.

The code is basically a copy of the input providers from the
`Kivy <https://github.com/kivy/kivy/tree/master/kivy/input>`_ project to make
the awesome work from there available for usage outside the kivy world.

Differences to the original implementation are:

* Motion events are not fired via a Window object, but a dedicated dispatcher
  located in ``nuiinput.dispatcher``. When wiring ``nuiinput`` into a main
  loop, this is the place to deal with receiving motion events.
