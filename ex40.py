import sys

# Verifica se o número de argumentos é menor que 3
if len(sys.argv) < 3:
    print('Entrada inválida. Por favor, forneça nome e sobrenome.')
else:
    # Atribui os valores de nome e sobrenome
    name = sys.argv[1]
    sobrenome = sys.argv[2]
    
    # Exibe o nome e sobrenome de duas formas
    print(name, sobrenome)
    print(f'{name} {sobrenome}')
