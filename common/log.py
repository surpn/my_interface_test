import logging
import os
import threading

from common.readConfig import Config
from common.utils import timestamp, current_path


class Logging(object):
	# logging 配置文件
	__config = Config().logging()
	__output_format = __config["output_format"]
	__dir = __config["dir"]
	__log_path = current_path(__dir)
	__logger = None

	def __init__(self):
		# 创建日志文件夹
		if not os.path.exists(self.__log_path):
			os.mkdir(self.__log_path)

		# 初始化
		self.__logger = logging.getLogger(__name__)
		self.__logger.setLevel(logging.DEBUG)

		# 设置log输出日志 级别.路径.格式化
		handler = logging.FileHandler(filename=self.__log_path + timestamp() + ".log", encoding='utf-8')
		formatter = logging.Formatter(self.__output_format)
		handler.setFormatter(formatter)

		# 设置控制台日志 级别.路径.格式化
		console = logging.StreamHandler()
		console.setLevel(logging.INFO)

		self.__logger.addHandler(handler)
		self.__logger.addHandler(console)

	def debug(self, msg, *args, **kwargs):
		self.__logger.debug(msg, *args, **kwargs)

	def info(self, msg, *args, **kwargs):
		self.__logger.info(msg, *args, **kwargs)

	def warning(self, msg, *args, **kwargs):
		self.__logger.warning(msg, *args, **kwargs)

	def error(self, msg, *args, **kwargs):
		self.__logger.error(msg, *args, **kwargs)




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
	def log():
		return Log.log


if __name__ == '__main__':
	log = Log().log()
	log.debug("debug")
	log.info("info")
	log.warning("warning")
	log.error("error")
