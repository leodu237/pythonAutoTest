# -*- coding:utf-8 -*-
#带header的get

import requests
import json

host = "http://httpbin.org/"
endpoint = "get"

url = ''.join([host,endpoint])
headers = {"User-Agent":"test request headers","Accept":"text/plain"}


r = requests.get(url=url)
r = requests.get(url = url,headers = headers)


print ((eval(r.text))["headers"]["Accept"])