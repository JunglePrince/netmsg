import unittest

class TestClass(unittest.TestCase):
	def test_always_pass(self):
		self.assertTrue(True)

# provide the textual feedback when running the tests
if __name__ == '__main__':
    unittest.main()