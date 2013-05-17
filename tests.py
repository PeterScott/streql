"""Tests for string comparison."""

from streql import equals
import unittest
import sys

PYTHON3 = sys.version_info[0] == 3


def b(s):
  """Bytes from a string."""
  if PYTHON3:
    return bytes(s, 'utf8')
  if isinstance(s, unicode):
    return s.encode('utf8')
  return str(s)


def u(s):
  """Unicode string from a string."""
  if PYTHON3:
    return s
  if isinstance(s, str):
    return s.decode('utf8')
  return unicode(s)



class BytewiseEqualityTest(unittest.TestCase):
  """Test equality of some strings and arrays."""

  def testEqualStrings(self):
    self.assertTrue(equals(b('foo'), b('foo')))
    self.assertTrue(equals(u('foo'), u('foo')))
    self.assertTrue(equals(b('foo'), u('foo')))
    self.assertTrue(equals(u('foo'), b('foo')))
    self.assertTrue(equals('hello'*1000, 'hello'*1000))
    if PYTHON3:
      self.assertTrue(equals(bytes('hello\xa0world', 'utf8'), 'hello\xa0world'))
    else:
      self.assertTrue(equals('hello\xc2\xa0world', 'hello\xc2\xa0world'.decode('utf8')))

  def testUnequalStrings(self):
    self.assertFalse(equals(b('foo'), b('bar')))
    self.assertFalse(equals(u('foo'), u('bar')))
    self.assertFalse(equals(b('hello, world!'), b('hello, world.')))
    self.assertFalse(equals(b('aaa'), b('aa')))
    self.assertFalse(equals(u('aaa'), u('aa')))

  def testWithEmptyStrings(self):
    self.assertTrue(equals(b(''), b('')))
    self.assertFalse(equals(b('a'), b('')))
    self.assertFalse(equals(b(''), b('a')))
    self.assertTrue(equals(u(''), u('')))
    self.assertFalse(equals(u('a'), u('')))
    self.assertFalse(equals(u(''), u('a')))

