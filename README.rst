Constant-time string comparison
-------------------------------

.. image:: https://travis-ci.org/PeterScott/streql.png
   :target: https://travis-ci.org/PeterScott/streql

Sometimes you need to test strings for equality with an algorithm whose timing depends
only on the length of the strings, and not on the contents of the strings themselves. If
one of those strings is of constant width -- an
`HMAC <http://en.wikipedia.org/wiki/HMAC>`_, for example -- then it becomes a constant-time
operation. This can be used to prevent some `timing side-channel
attacks <http://en.wikipedia.org/wiki/Timing_attack>`_, such as `the critical vulnerability
found in KeyCzar back in 2009 <http://codahale.com/a-lesson-in-timing-attacks/>`_.

This module offers a single function, ``equals(x, y)``, which takes two strings ``x`` and
``y`` and returns ``True`` if they are equal, and ``False`` if they are not. The time
this function takes does not depend on what specific bytes are in these strings. Unicode
strings are encoded with the default codec (ASCII in Python 2, UTF-8 in Python 3) before
being compared; it is recommended that you only use this on byte strings (``str`` in
Python 2, ``bytes`` in Python 3).

This works with Python 2 and 3, and PyPy. The license is Apache 2.0.
