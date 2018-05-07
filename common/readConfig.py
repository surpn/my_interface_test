# _*_coding:utf-8_*_
import os
import configparser

from common.utils import current_path


class Config(object):
	"""
	获取配置 ini 文件
	read(filename)：读取ini文件中的内容
	sections()：得到所有section，返回列表形式
	[('key', 'value')]
	options(section)：得到给定section的所有option
	items(section):得到指定section的所有key-value
	get(section,option)：得到section中的option值，返回str类型
	get(section,option)：得到section中的option值，返回int类型
	"""

	def __init__(self):
		# 本地文件夹路径
		self.dir_path = current_path("config")
		if not os.path.exists(self.dir_path):
			os.mkdir(self.dir_path)

	def get_ini(self, ini_filename):
		file_path = self.dir_path + ini_filename
		cf = configparser.ConfigParser(interpolation=None)
		cf.read(file_path, encoding='UTF-8')
		return cf

	def mysqldb(self):
		cf = self.get_ini("db.ini")
		items = cf.items("mysqlconf")
		cfg = {}
		for item in items:
			cfg[item[0]] = item[1]
		return cfg

	def url(self):
		cf = self.get_ini("url.ini")
		items = cf.items("urls")
		cfg = {}
		for item in items:
			cfg[item[0]] = item[1]
		return cfg

	def email(self):
		cf = self.get_ini("email.ini")
		items = cf.items("email")
		cfg = {}
		for item in items:
			cfg[item[0]] = item[1]
		return cfg

	def logging(self):
		cf = self.get_ini("logging.ini")
		items = cf.items("logging")
		cfg = {}
		for item in items:
			cfg[item[0]] = item[1]
		return cfg


if __name__ == "__main__":
	config = Config().mysqldb()
	print(config)
	config = Config().url()
	print(config)
	config = Config().email()
	print(config)
	config = Config().logging()
	print(config)
