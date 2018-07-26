from stone import *
import unittest

class TestPlayer(unittest.TestCase):
	""" Test Player Class Methods """

	def test_authentication(self):
		self.assertTrue(Player.authentication(self, 'aaa'))

	def test_goBackToMenu(self):
		self.assertTrue(Player.goBackToMenu(self, '0'))

	def test_calculateWinsRate(self):
		self.assertEqual(Player.calculateWinsRate(self, 'aaa'), 0)


if __name__ == '__main__':
	unittest.main()
