import hashlib

#https://docs.python.org/3/library/hashlib.html
user_password = "pa$$w0rd"
h = hashlib.md5(user_password.encode())
hash = h.hexdigest()
print(hash)
