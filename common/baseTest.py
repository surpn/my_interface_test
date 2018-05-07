import unittest

import requests

from common.log import MyLog
from common.readConfig import Config


class BaseTest(unittest.TestCase):
	"""
	测试基类
	"""
	def setUp(self):
		self.log = MyLog().get_log().logger
		cfg = Config()
		test_url = cfg.url("test")
		method = "/ICCardCheckIn"
		self.url = test_url + method
		self.s = requests.session()
		r = self.s.post("http://localhost:9090/iccard/InitSystem")
		self.log.info(r.text)

		self.log.info(u"setUp success")

	def tearDown(self):
		self.s.close()
		self.log.info(u"tearDown  success")
