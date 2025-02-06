#set
planeta_anao = { 'pluta', 'mercurio', 'venus', 'terra', 'marte', 'jupiter', 'saturno', 'urano', 'netuno'}
print(len(planeta_anao))

print('terra' in planeta_anao)
print('terra' not in planeta_anao)

for astro in planeta_anao:
    print(astro.capitalize())
    print(astro.upper())
    print(astro.lower())

print(planeta_anao, end=' ')
planeta_anao.add('plutao')
planeta_anao.add('ceres')
planeta_anao.remove('plutao')
planeta_anao.pop()
planeta_anao.clear()
print(planeta_anao)

planeta_anao.update('ceres')

planetas = { 'pluta', 'mercurio', 'venus', 'terra', 'marte', 'jupiter', 'saturno', 'urano', 'netuno'}

print( planeta_anao | planetas)
print( planeta_anao.union(planetas))
print( planeta_anao & planetas)
print( planeta_anao.intersection(planetas))
print( planeta_anao - planetas)
print( planeta_anao.difference(planetas))
print( planeta_anao ^ planetas)
print( planeta_anao.symmetric_difference(planetas))
