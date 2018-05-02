import logging
import os
import threading

from common.readConfig import Config
from common.utils import current_path, timestamp


class Logging(object):

	log_path = current_path(r"\logs")
	config = Config().logging()
	print(config)
	output_format = config[0]
	__logger = None

	def __init__(self):
		global log_path, output_format, __logger
		# 创建日志文件夹
		if not os.path.exists(log_path):
			os.mkdir(log_path)

		# 初始化
		__logger = logging.getLogger(__name__)
		__logger.setLevel(logging.INFO)

		# 设置输出日志 级别.路径.格式化
		handler = logging.FileHandler(filename=log_path + timestamp() + ".log", encoding='utf-8')
		formatter = logging.Formatter(output_format)
		handler.setFormatter(formatter)

		# 设置显示日志 级别.路径.格式化
		console = logging.StreamHandler()
		console.setLevel(logging.INFO)

		__logger.addHandler(handler)
		__logger.addHandler(console)

	@staticmethod
	def get_logger(self):
		"""
		get logger
		:return:
		"""
		return Logging.__logger

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


class Log(object):

	log = None
	mutex = threading.Lock()

	def __init__(self):
		if Log.log is None:
			Log.mutex.acquire()
			Log.log = Logging()
			Log.mutex.release()

	@staticmethod
	def get_log():
		return Log.log


if __name__ == '__main__':
	log = Log().get_log()
	log.info("12")
