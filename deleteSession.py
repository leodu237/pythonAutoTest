#-*- coding:utf-8 -*-

import requests
import json

host = "http://httpbin.org/"
endpoint = "headers"

url = ''.join([host,endpoint])

headers1 = {"testA":"AAA"}
headers2 = {"testB":"BBB"}

s = requests.session()
s.headers.update(headers1)
r = s.get(url, headers = headers2)

print (r.text)

print('---------------------------------------------------')

s.headers['testA'] = None
r1 = s.get(url,headers = headers2)
print(r1.text)