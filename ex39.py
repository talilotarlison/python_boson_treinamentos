# A condição if len(sys.argv) < 1 deveria ser if len(sys.argv) < 3, porque sys.argv[0] sempre será o nome do script. 
# Para garantir que o nome e sobrenome sejam passados corretamente, você precisa de pelo menos 3 argumentos.

# sys.argv[1] e sys.argv[2] são os argumentos do nome e sobrenome, então a ordem está correta.

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


# A condição agora verifica se há pelo menos 3 argumentos (incluindo o nome do script).

# A mensagem de erro foi melhorada para esclarecer o que está faltando.

# As variáveis name e sobrenome são atribuídas após a verificação, garantindo que o código funcione apenas quando os argumentos corretos forem fornecidos.