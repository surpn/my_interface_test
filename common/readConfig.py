import os
import configparser

from common.utils import url2ip, current_path


class Config(object):

	def __init__(self):
		# 本地文件夹路径
		self.dir_path = current_path("config")
		self.cf = configparser.ConfigParser()

	def db(self):
		file_path = self.dir_path + r"db.ini"
		self.cf.read(file_path)

		host = self.cf.get("sqlconf", "host")
		ip = url2ip(host)
		port = self.cf.get("sqlconf", "port")
		db_name = self.cf.get("sqlconf", "db_name")
		user = self.cf.get("sqlconf", "user")
		password = self.cf.get("sqlconf", "password")
		cfg = (ip, port, db_name, user, password)
		return cfg

	def url(self, target_url="test"):
		file_path = self.dir_path + r"url.ini"
		self.cf.read(file_path)
		url = self.cf.get("urls", target_url)
		return url

	def email(self):
		file_path = self.dir_path + r"email.ini"
		self.cf.read(file_path)
		smtp_server = self.cf.get("email", "smtp_server")
		user = self.cf.get("email", "user")
		password = self.cf.get("email", "password")
		sender = self.cf.get("email", "sender")
		receiver = eval(self.cf.get("email", "receiver"))
		cfg = (smtp_server, user, password, sender, receiver)
		return cfg


if __name__ == "__main__":

	config = Config()
	print(type(config.email()[4]))
