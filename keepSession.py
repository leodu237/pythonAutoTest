#-*- coding:utf-8 -*-

import requests
import json

host = "http://httpbin.org/"
endpoint = "cookies"

url = ''.join([host,endpoint])
url1 = "http://httpbin.org/cookies/set/sessioncookie/123456789"

r = requests.get(url)
print (r.text)

print ("------")

s = requests.session()
s.get(url1)
r = s.get(url)

print (r.text)

