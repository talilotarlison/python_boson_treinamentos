var1 = 10
var2 = 20
# sem usar a variável auxiliar
var1, var2 = var2, var1
print(var1, var2)

# ternario em python
menor = var1 if var1 < var2 else var2
print(menor)

# generators

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = (x ** 2 for x in valores)
print(quadrados)

for x in quadrados:
    print(x)
# output: 1 4 9 16 25 36 49 64 81 100

# funcao inumerate
bebidas = ['cafe', 'suco', 'refrigerante', 'agua']
for i, bebida in enumerate(bebidas):
    print(i, bebida)
# output: 0 cafe 1 suco 2 refrigerante 3 agua

temperaturas = [10, 20, 30, 40, 50,-60, -70, 80, 90, 100]
for i, temp in enumerate(temperaturas):
    if temp < 0:
        print(f"Temperatura negativa na posição {i}")