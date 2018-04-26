import xeger


def han(i=1):

	s = ""
	for j in range(i):
		a = xeger.xeger(u"[\\u4e00-\\u9fa5]{1}")
		s = s + a

	return s


def shu(i=1):
	s = ""
	for j in range(i):
		a = xeger.xeger(u"[0-9]{1}")
		s = s + a

	int(s)

	return s


if __name__ == '__main__':

	print(han(2))
	print(shu(2))
