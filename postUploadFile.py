#-*- coding:utf-8 -*-

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])
files = {
	'file':open('/Users/dulongnian/pstest/text.txt','rb')
}

r = requests.post(url,files = files)

print(r.text)