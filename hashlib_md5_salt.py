import hashlib

#https://docs.python.org/3/library/hashlib.html
user_entered_password = "pa$$w0rd"
salt = "5gz"
db_password = user_entered_password+salt
h = hashlib.md5(db_password.encode())


hash = h.hexdigest()
print(hash)
