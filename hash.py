import hashlib
data="hello"

m=hashlib.md5()#md5
m=hashlib.sha256()#sha256
m.update(data.encode("utf-8"))
h=m.hexdigest()
print(h)
