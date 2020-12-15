#-*- coding:utf-8 -*-

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])
params = {'key1':'value1','key2':'value2'}

r = requests.post(url,params = params)

print(r.text)