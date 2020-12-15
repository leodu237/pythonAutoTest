# -*- coding:utf-8 -*-
#带参数的get

import requests
import json

host = "http://httpbin.org/"
endpoint = "get"

url = ''.join([host,endpoint])
params = {"show_env":"1"}
headers = {"User-Agent":"test request headers","Accept":"text/plain"}

r = requests.get(url = url,params = params,headers = headers)
#response = r.json()

print (r.url)
print ((eval(r.text))["headers"]["User-Agent"])