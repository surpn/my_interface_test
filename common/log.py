import logging

import os
import threading

from common.utils import current_path, timestamp


class Log(object):

	def __init__(self):
		# 初始化
		self.logger = logging.getLogger(__name__)
		# 设置日志路径.级别.格式化
		self.logger.setLevel(logging.INFO)
		self.log_file_path = logging.FileHandler(current_path(r"\result\log") + timestamp() + ".log")
		formate = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		log_file_path.setFormatter(formate)
		self.logger.addHandler(log_file_path)

	def get_logger(self):
		"""
		get logger
		:return:
		"""
		return self.logger

	def build_start_line(self, case_no):
		"""
		write start line
		:return:
		"""
		self.logger.info("--------" + case_no + " START--------")

	def build_end_line(self, case_no):
		"""
		write end line
		:return:
		"""
		self.logger.info("--------" + case_no + " END--------")

	def build_case_line(self, case_name, **json):
		"""
		write test case line
		:param case_name:
		:param code:
		:param msg:
		:return:
		"""
		self.logger.info(case_name + " - json:" + str(json))

	def get_report_path(self):
		"""
		get report file path
		:return:
		"""
		# report_path = os.path.join(self.log_file_path, "report.html")
		return self.log_file_path

	def get_result_path(self):
		"""
		get test result path
		:return:
		"""
		return self.log_file_path

	def write_result(self, result):
		"""
		:param result:
		:return:
		"""
		result_path = os.path.join(self.log_file_path, "report.txt")
		fb = open(result_path, "wb")
		try:
			fb.write(result)
		except FileNotFoundError as ex:
			self.logger.error(str(ex))


class MyLog:

	log = None
	mutex = threading.Lock()

	def __init__(self):
		pass

	@staticmethod
	def get_log():

		if MyLog.log is None:
			MyLog.mutex.acquire()
			MyLog.log = Log()
			MyLog.mutex.release()

		return MyLog.log


if __name__ == '__main__':
	log = MyLog.get_log()
	log.build_case_line("instruct", **{'status': 200, 'text': '-1531917099'})
	print(log.get_result_path())
	# logger = log.get_logger()
	# logger.debug("test debug")
	# logger.info("test info")

