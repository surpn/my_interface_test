import requests

from interface_test.common.urls import url

url = url('test')
method = u"/ICCardCheckIn"
init = u"/InitSystem"
s = requests.session()
json = {"cardNo": 1001}
# headers = {
# 			"Accept-Encoding": "gzip,deflate",
# 			"Content-Type": "application/json",
# 			"Host": "localhost:9090",
# 			"Connection": "Keep-Alive",
# 		}

s.post(url=url+init)
r = s.post(url=url+method, json=json)
print(r.text)
