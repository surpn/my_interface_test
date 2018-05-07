import unittest

from common.HTMLTestRunner import HTMLTestRunner
from common.utils import current_path, timestamp


class TestRunner:
	"""
	测试驱动
	"""
	def __init__(self, test_dir="", title=None, description=None):

		if test_dir == "":
			self.test_dir = current_path(r"test_case")

		self.discover = unittest.defaultTestLoader.discover(self.test_dir, pattern='test*.py')
		self.title = title
		self.description = description
		# 定义报告存放的路径
		self.path = current_path(r"\result\report")

	def run(self):
		with open(self.path + timestamp() + '.html', 'wb') as fp:
			# 定义测试报告
			r = HTMLTestRunner(stream=fp, title=self.title, description=self.description)
			r.run(self.discover)


if __name__ == "__main__":
	runner = TestRunner(title="title", description="description")
