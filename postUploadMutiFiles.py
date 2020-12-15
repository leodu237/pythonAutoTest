#-*- coding:utf-8 -*-

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])
files = {
	('file1', ('text.txt',open('/Users/dulongnian/pstest/text.txt','rb'))),
	('file2', ('hello.txt',open('/Users/dulongnian/pstest/hello.txt','rb')))
}

r = requests.post(url,files = files)

print(r.text)