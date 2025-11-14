import hashlib

#https://docs.python.org/3/library/hashlib.html
m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
m.digest()

hash = m.hexdigest()
print(hash)
