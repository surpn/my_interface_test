import pymysql.cursors
from common.readConfig import Config

# ======== Reading db.ini setting ===========
config = Config().db()
host = config[0]
port = config[1]
db = config[2]
user = config[3]
password = config[4]


# ======== MySql base operating ===================

class DB:
	def __init__(self):
		try:

			# Connect to the database
			self.connection = pymysql.connect(

				host=host,
				user=user,
				password=password,
				db=db,
				charset='utf8mb4',
				cursorclass=pymysql.cursors.DictCursor)

		except pymysql.err.OperationalError as e:
			print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

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

	# close database
	def close(self):
		self.connection.close()


if __name__ == '__main__':

	# db = DB()
	# table_name = "sign_event"
	# data = {'id':1,'name':'红米','`limit`':2000,'status':1,
	# 'address':'北京会展中心','start_time':'2016-08-20 00:25:42'}
	# table_name2 = "sign_guest"
	# data2 = {'realname':'alen','phone':12312341234,'email':'alen@mail.com',
	# 'sign':0,'event_id':1}
	# db.clear(table_name)
	# db.insert(table_name, data)
	# db.close()

	connection = pymysql.connect(host="surpn.iok.la", port=33066,user="root", password="123456", db="test")
	try:
		# with connection.cursor() as cursor:
		# 	# Create a new record
		# 	sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
		# 	cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
		#
		# # connection is not autocommit by default. So you must commit to save
		# # your changes.
		# connection.commit()

		with connection.cursor() as cursor:
			# Read a single record
			sql = "SELECT `name`, `age` FROM `user`"
			cursor.execute(sql)
			result = cursor.fetchall()
			print(result)
	finally:
		connection.close()

	print(host)
