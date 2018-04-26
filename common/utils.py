import socket
import time
import os
import re
import xeger


def current_path(dpath=r"", mkdir=False):
	"""获取文件夹路径"""
	# 当前工作环境路径
	curr_path = os.path.dirname(os.path.dirname(os.path.join(os.path.abspath(__file__))))

	# dirs = dpath.split("\\")
	dirs = re.split(r'\\|/', dpath)
	if len(dirs) != 0:
		for d in dirs:
			print(d)
			curr_path = os.path.join(curr_path, d)

	curr_path = os.path.join(curr_path, "")
	# 判断路径文件夹是否存在
	if os.path.exists(curr_path):
		return curr_path
	else:
		if mkdir is True:
			os.makedirs(curr_path)
			return curr_path
			print(curr_path + "文件夹创建成功")
		else:
			print("文件夹不存在")


def timestamp():
	"""时间戳"""
	time_stamp = time.strftime("%Y%m%d%H%M%S")
	return time_stamp


def url2ip(url):
	"""域名转ip"""
	try:
		ip = socket.gethostbyname(url)
		return ip

	except socket.error as e:
		print(e)


def newest_file(loc):
	"""文件夹中最新的文件"""
	files = os.listdir(loc)
	if len(files) != 0:
		files.sort(key=lambda fn: os.path.getmtime(loc + fn))
		file = files[-1]
		return location + file
		# print(location + file)


def random_chinese_characters(i=1):
	"""随机中文汉字"""
	s = ""
	if i < 11:
		s = xeger.xeger(u"[\\u4e00-\\u9fa5]{1}")

	else:
		j = i // 10
		k = i % 10

		while j > 0:
			a = xeger.xeger(u"[\\u4e00-\\u9fa5]{10}")
			s = s + a
			j -= 1
			if j == 0:
				a = xeger.xeger(u"[\\u4e00-\\u9fa5]{}".format("{"+str(k)+"}"))
				s = s + a
	return s


if __name__ == "__main__":
	# print(timestamp())
	# print(url2ip('surpn.iok.la'))
	# location = current_path("/result\log")
	# print(location)
	# current_path(location)
	start = time.clock()

	print(start)
	print(random_chinese_characters(100))

	elapsed = (time.clock() - start)
	print("Time used:", elapsed)
