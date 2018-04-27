# -*- coding:utf-8 -*-
import unittest

from common.baseTest import BaseTest


class TestICCardCheckIn(BaseTest):
	"""校验IC卡的有效性"""

	def test_ICCardCheckIn01(self):
		"""输入{"cardNo":1001}"""
		r = self.s.post(url=self.url, json=self.json)
		self.log.info(r.text)
		self.assertEqual(u'{"expectResult":"0","expectSysMessage":"插卡成功！"}', r.text, "123")

	def test_ICCardCheckIn02(self):
		"""输入{"cardNo":1000}"""
		r = self.s.post(url=self.url, json=self.json)
		self.log.info(r.text)
		self.assertEqual(u'{"expectResult":"0","expectSysMessage":"插卡成功！"}', r.text, "123")


if __name__ == "__main__":
	# unittest.main()
	suite = unittest.TestSuite()
	suite.addTest(TestICCardCheckIn('test_ICCardCheckIn01'))
	# 执行测试
	runner = unittest.TextTestRunner()
	runner.run(suite)
