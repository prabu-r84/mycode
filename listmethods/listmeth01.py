#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
print(proto)
print(type(proto))
print(proto[1])
print(type(proto))
proto.extend("dns") # this line will add d, n, and s
print(proto)
