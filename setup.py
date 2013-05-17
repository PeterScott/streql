"""
Constant-time string comparison
-------------------------------

Sometimes you need to test strings for equality with an algorithm whose timing depends
only on the length of the strings, and not on the contents of the strings themselves. If
one of those strings is of constant width -- an
`HMAC <http://en.wikipedia.org/wiki/HMAC>`_, for example -- then it becomes a constant-time
operation. This can be used to prevent some `timing side-channel
attacks <http://en.wikipedia.org/wiki/Timing_attack>`_, such as `the critical vulnerability
found in KeyCzar back in 2009 <http://codahale.com/a-lesson-in-timing-attacks/>`_.

This module offers a single function, ``equals(x, y)``, which takes two strings ``x`` and
``y`` and returns ``True`` if they are equal, and ``False`` if they are not. The time
this function takes does not depend on what specific bytes are in these strings. Strings
are encoded with UTF-8 before being compared. This works on both Unicode and byte
strings, in Python 2 and 3.

The module is written in C, for speed and predictability. The license is Apache 2.0.
"""

try:
  from setuptools import setup, Extension
except ImportError:
  from distutils.core import setup
  from distutils.extension import Extension

setup(
    name = 'streql',
    version = '2.0',
    description = 'Constant-time string comparison',
    long_description = __doc__,
    author = 'Peter Scott',
    author_email = 'peter@cueup.com',
    license = 'Apache',
    url = 'https://github.com/PeterScott/streql',
    test_suite = 'tests',
    zip_safe = False,
    ext_modules = [Extension("streql", ["streql.c"])],
    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'License :: OSI Approved :: Apache Software License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Security',
      'Topic :: Security :: Cryptography',
    ],
)
