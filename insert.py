#!/usr/bin/python3


from pymemcache.client import base
#from memcache import Client

#client = memcache.client(['localhost:11211'])
mc = base.Client(('localhost',11211))
mc.set("a",100)
X = mc.get("a").decode()
#decode() - function that converts bytes to string , cause memchace paramets type is 'Bytes'
print(X)
