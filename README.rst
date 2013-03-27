Constant-time string comparison
-------------------------------

Sometimes you need to test strings for equality with an algorithm whose timing depends
only on the length of the strings, and not on the contents of the strings themselves. If
one of those strings is of constant width -- an
`HMAC <http://en.wikipedia.org/wiki/HMAC>`, for example -- then it becomes a constant-time
operation. This can be used to prevent some [timing side-channel
attacks](http://en.wikipedia.org/wiki/Timing_attack>`, such as `the critical vulnerability
found in KeyCzar back in 2009 <http://codahale.com/a-lesson-in-timing-attacks/>`.

This module offers a single function, ``equals(x, y)``, which takes two strings ``x`` and
``y`` and returns ``True`` if they are equal, and ``False`` if they are not. The time
this function takes does not depend on what specific bytes are in these strings.

Technically, this should work for any object that supports the read-only buffer
interface, so it should also work for arrays.

The module is written in C, for speed and predictability. The license is Apache 2.0.
