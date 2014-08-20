import sys
sys.path.append('../src')

import unittest
from network_utils import * 
from netmsg_constants import *

class TestNetworkUtils(unittest.TestCase):
	def test_parse_and_validate_port_range(self):
		#valid range
		self.assertTrue(parse_and_validate_port("1024"))
		self.assertTrue(parse_and_validate_port("65535"))
		#invalid range
		self.assertFalse(parse_and_validate_port("1023"))
		self.assertFalse(parse_and_validate_port("65536"))

	def test_parse_and_validate_port_non_int(self):
		self.assertFalse(parse_and_validate_port("doba"))
		self.assertFalse(parse_and_validate_port("doba1024"))
		self.assertFalse(parse_and_validate_port("1024doba"))

# provide the textual feedback when running the tests
if __name__ == '__main__':
    unittest.main()