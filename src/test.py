class TestA(object):

	def __init__(self):

		data = (
				('guping', 12),
				('zhangsan', 16),
				('lisi', 11),
				('wangwu', 23)
				)

		self.dic = {}
		for i in data:
			self.dic["name"] = i[0]
			self.dic["age"] = i[1]

			print(self.dic)

	def __getitem__(self, key):
		if key in self.dic:
			return self.dic[key]

	def __setitem__(self, key, value):
		self.dic[key] = value


if __name__ == "__main__":
	a = TestA()
	a["name"] = 123
	print(a["name"])
