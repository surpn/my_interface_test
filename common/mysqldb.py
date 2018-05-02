# -*- coding: UTF-8 -*-
import pymysql.cursors
from common.readConfig import Config

# ======== Reading db.ini setting ===========
config = Config().mysqldb()
host = config["host"]
port = int(config["port"])
user = config["user"]
password = config["password"]
db = config["db"]
charset = config["charset"]
cursorclass = config["cursorclass"]
if cursorclass == "dict":
	cursorclass = pymysql.cursors.DictCursor
if cursorclass == "tuple":
	cursorclass = pymysql.cursors.Cursor


# ======== MySql base operating ===================

class MysqlDB(object):
	# Connect to the database
	def __init__(self):
		try:

			self.connection = pymysql.connect(

				host=host,
				port=port,
				user=user,
				password=password,
				db=db,
				charset=charset,
				cursorclass=cursorclass)

			# print(config)
		except pymysql.err.OperationalError as e:
			print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

	# close database
	def close(self):
		self.connection.close()

	# select sql statement
	def select(self):
		pass

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
			table_data[key] = "'"+str(table_data[key])+"'"
			key = ','.join(table_data.keys())
			value = ','.join(table_data.values())
			real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value
			+ ")"

		# print(real_sql)
		with self.connection.cursor() as cursor:
			cursor.execute(real_sql)
			self.connection.commit()


if __name__ == '__main__':
	conn = MysqlDB().connection
	try:
		with conn.cursor() as cursor:
			# Read a single record
			sql = "SELECT `name`, `age` FROM `user`"
			cursor.execute(sql)
			# result = cursor.fetchone()
			# print(result)
			result = cursor.fetchall()
			print(result)
	finally:
		conn.close()
