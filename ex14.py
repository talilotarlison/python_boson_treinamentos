#dicionarios

elemento = {
    'H': 'Hidrogenio',
    'He': 'Helio',
    'Li': 'Litio',
    'Be': 'Berilio',
}

print(elemento['H'])
print(len(elemento))

del elemento['He']
elemento.clear()
del elemento
print(elemento.items())

for i in elemento.items():
    print(i)

for i in elemento.keys():
    print(i)

for i in elemento.values():
    print(i)
