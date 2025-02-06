numeros =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = [x ** 2 for x in numeros]
print(quadrados)

nome = 'Python'
print(nome[0])

frase = 'Python é uma linguagem de programação'
vogais = "aeiou"
vogais = [x for x in frase if x in vogais]
print(vogais)
# output: ['o', 'e', 'u', 'a', 'i', 'a', 'e', 'a', 'e']
