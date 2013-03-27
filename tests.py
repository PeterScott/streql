"""Tests for string comparison."""

from streql import equals
from array import array
import unittest



class BytewiseEqualityTest(unittest.TestCase):
  """Test equality of some strings and arrays."""

  def testEqualStrings(self):
    self.assertTrue(equals('foo', 'foo'))
    self.assertTrue(equals('hello'*1000, 'hello'*1000))

  def testUnequalStrings(self):
    self.assertFalse(equals('foo', 'bar'))
    self.assertFalse(equals('hello, world!', 'hello, world.'))
    self.assertFalse(equals('aaa', 'aa'))

  def testWithEmptyStrings(self):
    self.assertTrue(equals('', ''))
    self.assertFalse(equals('a', ''))
    self.assertFalse(equals('', 'a'))

  def testWithArrays(self):
    self.assertTrue(equals(array('c', 'hello'), array('c', 'hello')))
    self.assertFalse(equals(array('c', 'hello'), array('c', 'world')))
    self.assertTrue(equals(array('i', [1, 2, 3]), array('i', [1, 2, 3])))
    self.assertFalse(equals(array('i', [1, 2, 3]), array('i', [3, 2, 1])))

  def testWithBuffers(self):
    self.assertTrue(equals(buffer('foo'), buffer('foo')))
    self.assertFalse(equals(buffer('foo'), buffer('bar')))
