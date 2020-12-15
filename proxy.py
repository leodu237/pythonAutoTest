# -*- coding:utf-8 -*-

import requests

proxies = {
	"https":"http://41.118.132.70:4433"
}

r = requests.post("http://httpbin.org/post",proxies = proxies)
r1 = requests.post("http://httpbin.org/post")

print (r.text)
print('---------------------------')
print (r1.text)