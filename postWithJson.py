#-*- coding:utf-8 -*-

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])
data = {
	"sites":[
		{"name":"test" , "url":"www.test.com"},
		{"name":"google", "url":"www.google.com"},
		{"name":"baidu", "url":"www.baidu.com"}
	]
}

r = requests.post(url,json=data)

print (r.json())