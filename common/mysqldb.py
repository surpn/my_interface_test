# -*- coding: UTF-8 -*-
import pymysql.cursors
from DBUtils import PooledDB

from common.readConfig import Config


class MysqlDB(object):
	"""
	MySQL配置
	"""
	# 读取配置文件
	__config = Config().mysqldb()   # 配置文件
	__host = __config["host"]   # 主机地址
	__port = int(__config["port"])  # 端口
	__user = __config["user"]  # 用户名
	__password = __config["password"]  # 密码
	__db = __config["db"]  # 数据库名
	__charset = __config["charset"]   # 编码
	__cursorclass = __config["cursorclass"]   # 返回数据格式(字典,元祖)
	if __cursorclass == "dict":
		__cursorclass = pymysql.cursors.DictCursor
	if __cursorclass == "tuple":
		__cursorclass = pymysql.cursors.Cursor
	__conn = None
	__cursor = None

	def __init__(self):
		# 初始化数据库连接
		self.__config = dict({
			"host": self.__host,
			"port": self.__port,
			"user": self.__user,
			"password": self.__password,
			"db": self.__db,
			"charset": self.__charset,
			"cursorclass": self.__cursorclass
		})
		try:
			self.__conn = PooledDB.connect(creator=pymysql, **self.__config)
			self.__cursor = self.__conn.cursor()

		except pymysql.err.OperationalError as e:
			print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

	# 关闭数据库连接
	def close(self):
		if self.__cursor:
			self.__cursor.close()
		if self.__conn:
			self.__conn.close()

	# select sql statement
	def select_one(self):
		sql = "SELECT `name`, `age` FROM `user`"
		self.__cursor.execute(sql)
		# result = cursor.fetchone()
		# print(result)
		result = self.__cursor.fetchall()
		return result

	# clear table data
	def clear(self, table_name):
		# real_sql = "truncate table " + table_name + ";"
		real_sql = "delete from " + table_name + ";"
		with self.connection.cursor() as c:
			c.execute("SET FOREIGN_KEY_CHECKS=0;")
			c.execute(real_sql)
		self.connection.commit()

	# insert sql statement
	def insert(self, table_name, table_data):
		for key in table_data:
			table_data[key] = "'" + str(table_data[key]) + "'"
			key = ','.join(table_data.keys())
			value = ','.join(table_data.values())
			real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value
			+ ")"

		# print(real_sql)
		with self.connection.cursor() as cursor:
			cursor.execute(real_sql)
			self.connection.commit()


if __name__ == '__main__':
	conn = MysqlDB()
	try:
		result = conn.select_one()
		print(result)
	finally:
		conn.close()
