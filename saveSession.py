#-*- coding:utf-8 -*-

import requests
import json

host = "http://httpbin.org/"
endpoint = "headers"

url = ''.join([host,endpoint])

headers1 = {"testA":"AAA"}
headers2 = {"testB":"BBB"}
headers3 = {"testC":"CCC"}
headers4 = {"testD":"DDD"}

s = requests.session()
s.headers.update(headers1)

r = s.get(url,headers = headers2)
s.headers.update(headers3)
r = s.get(url,headers = headers4)

print (r.text)