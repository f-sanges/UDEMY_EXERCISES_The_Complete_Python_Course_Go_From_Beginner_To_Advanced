import urllib.request
from urllib.request import urlopen

f = urllib.request.urlopen('http://www.python.org')
print(f.read())


# check status
import http.client
from http.client import HTTPSConnection
conn = http.client.HTTPSConnection('www.python.org')
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)


# Cookies
from http import cookies
c = cookies.SimpleCookie()
c["fig"] = "newton"
c["sugar"] = "cone"
print(c)



# Parsing
import urllib.request
import urllib.parse

url = 'http://www.python.org'
values ={'s': 'basic',
         'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
