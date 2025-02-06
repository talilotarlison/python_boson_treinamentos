notas = [ 5,6,7,5,6,4]
print(notas)

notas2= [2,4,6,3]

valores = notas + notas2
print(valores)

print(valores[1])
# ultimo valor
print(valores[-1])
# slice
print(valores[0:2])

print(valores[4:])

print(len(valores))
print(sorted(valores, reverse=True))

print(sum(valores))
print(min(valores))
print(max(valores))

valores.append(13)
# remove ultimo
valores.pop()

valores.pop(5)

valores.insert(3,45)

print(12 in valores)

