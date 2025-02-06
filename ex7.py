import random

valor = random.randint(1,20)
print(valor)

print("gerar 5 numeros aleatorios")

for i in range(5):
    n = random.randint(1,50)
    print(n)

#Typecasting 

for i in range(5):
    f = random.random()
    print(round(f*10,2))

for i in range(5):
    h = random.uniform(1,100)
    print(round(h*10,2))
