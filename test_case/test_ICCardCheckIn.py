import pprint
import unittest

import requests

from interface_test.common.urls import url


class TestICCardCheckIn(unittest.TestCase):

	def setUp(self):

		self.test_url = url("test")
		self.method = "/ICCardCheckIn"
		self.s = requests.session()
		self.s.post(self.test_url + "/InitSystem")
		self.data = {

			"cardNo": 1001
		}

	def tearDown(self):
		self.s.close()

	def test_ICCardCheckIn01(self):

		u = self.test_url + self.method
		json = self.data
		r = self.s.post(url=u, json=json)
		r_data = r.text
		pprint.pprint(r.text)
		self.assertEqual('{"expectResult":"0","expectSysMessage":"插卡成功！"}', r_data, "123")
