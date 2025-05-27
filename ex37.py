# https://pythonhelp.wordpress.com/2011/11/15/argumentos-da-linha-de-comando/

# Isso mesmo, como podemos ver, o primeiro argumento para o programa é o próprio nome do programa, e é acessado através de sys.argv[0]. 
# A variável argv nada mais é do que uma lista. Sendo assim, seus elementos podem ser acessados via índice. 
# E o que acontece se chamarmos o programa acima sem argumentos?

# $ python args.py
# args.py
# Traceback (most recent call last):
#   File "args.py", line 5, in <module>
#     print sys.argv[1]
# IndexError: list index out of range

# Temos um erro de execução, pois nosso código tenta acessar elementos inexistentes na lista argv. 
# O que fazer? Antes de acessar um elemento, devemos checar se a lista o contém.

import sys
if len(sys.argv) >= 3:
    print sys.argv[0]
 print sys.argv[1]
 print sys.argv[2]

# Mas e aqueles programas que possuem diversas opções pela linha de comando, sendo algumas obrigatórias, outras opcionais,
#  como fazem? Tratam opção por opção?

# Até podem fazer isso de forma manual, mas existem ferramentas para manipulação de argumentos vindos da linha de comando
# que facilitam bastante o trabalho. Uma delas será o tema do próximo post: a argparse.