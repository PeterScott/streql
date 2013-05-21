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
this function takes does not depend on what specific bytes are in these strings. Unicode
strings are encoded as UTF-8 before being compared; it is recommended that you only use
this on byte strings (``str`` in Python 2, ``bytes`` in Python 3).

This works with Python 2 and 3, and PyPy. The license is Apache 2.0.
"""

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

common = dict(
    name = 'streql',
    version = '3.0.2',
    description = 'Constant-time string comparison',
    long_description = __doc__,
    author = 'Peter Scott',
    author_email = 'peter@cueup.com',
    license = 'Apache',
    url = 'https://github.com/PeterScott/streql',
    test_suite = 'tests',
    zip_safe = False,
    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'License :: OSI Approved :: Apache Software License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: Implementation :: CPython',
      'Programming Language :: Python :: Implementation :: PyPy',
      'Topic :: Security',
      'Topic :: Security :: Cryptography',
    ],
)

try:
  import __pypy__
  setup(py_modules=['streql'], package_dir={'':'pypy'}, **common)
except ImportError:
  try:
    from setuptools import Extension
  except ImportError:
    from distutils.extension import Extension
  setup(ext_modules = [Extension("streql", ["streql.c"])], **common)
