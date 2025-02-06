# funcao reduce
# importe lib functools
from functools import reduce

def multiplicar(x,y):
    return x*y

numeros_2 = [1,2,3,4,5,6,7,8,9,10]

acumulador = reduce(multiplicar, numeros_2)
print(acumulador)

# funcao lambda
quadrado = lambda x: x**2

for i in range(1,11):
    print(f'{i} ao quadrado = {quadrado(i)}')

par = lambda x: x%2 == 0
print(par(2))

far_c = lambda x: (x-32)*5/9
print(far_c(32))

celsius = lambda x: x*9/5 + 32
print(celsius(0))

# funcao map

lista = [1,2,3,4,5,6,7,8,9,10]
quadrados = map(lambda x: x**2, lista)
print(list(quadrados))

dobro = map(lambda x: x*2, lista)
print(list(dobro))

palavras = ['oi', 'ola', 'tchau']
maiusculas = map(lambda x: x.upper(), palavras)
print(list(maiusculas))

# funcao filter
def num_parente(x):
    return x%2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10]

pares = filter(num_parente, numeros)
print(list(pares))

num_impar = filter(lambda x: x%2 != 0, numeros)
print(list(num_impar))

# soma acumulativa dos quadrados dos numeros pares
soma = reduce(lambda x,y: x+y, map(lambda x: x**2, filter(lambda x: x%2 == 0, numeros)))
print(soma)