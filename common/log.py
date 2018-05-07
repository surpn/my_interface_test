import logging
import os
import threading

from common.readConfig import Config
from common.utils import timestamp, current_path


class Logging(object):
	"""
	日志输出配置
	"""
	# logging 配置文件
	__config = Config().logging()
	__output_format = __config["output_format"]
	__dir = __config["dir"]
	__log_path = current_path(__dir)
	__handler = __config["handler"]
	__console = __config["console"]
	_nameToLevel = {
		'CRITICAL': logging.CRITICAL,
		'FATAL': logging.FATAL,
		'ERROR': logging.ERROR,
		'WARN': logging.WARNING,
		'WARNING': logging.WARNING,
		'INFO': logging.INFO,
		'DEBUG': logging.DEBUG,
		'NOTSET': logging.NOTSET,
	}
	__handler_level = _nameToLevel[__config["handler_level"]]
	__console_level = _nameToLevel[__config["console_level"]]
	__logger = None

	def __init__(self):
		# 创建日志文件夹
		if not os.path.exists(self.__log_path):
			os.mkdir(self.__log_path)

		# 初始化
		self.__logger = logging.getLogger(__name__)
		self.__logger.setLevel(logging.DEBUG)

		# 设置log输出日志 级别.路径.格式化
		if self.__handler == "1":
			handler = logging.FileHandler(filename=self.__log_path + timestamp() + ".log", encoding='utf-8')
			handler.setLevel(self.__handler_level)
			formatter = logging.Formatter(self.__output_format)
			handler.setFormatter(formatter)
			self.__logger.addHandler(handler)

		# 设置控制台日志 级别.路径.格式化
		if self.__console == "1":
			console = logging.StreamHandler()
			console.setLevel(self.__console_level)
			self.__logger.addHandler(console)

	def debug(self, msg, *args, **kwargs):
		self.__logger.debug(msg, *args, **kwargs)

	def info(self, msg, *args, **kwargs):
		self.__logger.info(msg, *args, **kwargs)

	def warning(self, msg, *args, **kwargs):
		self.__logger.warning(msg, *args, **kwargs)

	def error(self, msg, *args, **kwargs):
		self.__logger.error(msg, *args, **kwargs)

	def get_logger(self):
		"""
		get logger
		:return:
		"""
		return self.__logger

	def build_start_line(self, case_no):
		"""
		write start line
		:return:
		"""
		self.__logger.info("--------" + case_no + " START--------")

	def build_end_line(self, case_no):
		"""
		write end line
		:return:
		"""
		self.__logger.info("--------" + case_no + " END--------")

	def build_case_line(self, case_name, **json):
		"""
		write test case line
		:param case_name:
		:param code:
		:param msg:
		:return:
		"""
		self.__logger.info(case_name + " - json:" + str(json))

	def get_report_path(self):
		"""
		get report file path
		:return:
		"""
		# report_path = os.path.join(self.log_file_path, "report.html")
		return self.__log_path


class Log(object):
	__log = None
	__mutex = threading.Lock()

	def __init__(self):
		if self.__log is None:
			self.__mutex.acquire()
			Log.__log = Logging()
			self.__mutex.release()

	@staticmethod
	def log():
		return Log.__log


if __name__ == '__main__':
	log = Log().log()
	log.debug("debug")
	log.info("info")
	log.warning("warning")
	log.error("error")
	print(log.get_logger())
