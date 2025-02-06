import random

l = [ 2,4,5,6,7,8,9]
n= random.choice(l)
print(n)

n= random.sample(l,3)
print(n)


random.shuffle(l)
print(l)

# https://www.w3schools.com/python/ref_random_shuffle.asp
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)

