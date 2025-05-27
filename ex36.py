import sys
print sys.argv[0]
print sys.argv[1]
print sys.argv[2]

# https://pythonhelp.wordpress.com/2011/11/15/argumentos-da-linha-de-comando/

# O exemplo acima mostra o uso do atributo argv do módulo sys. 
# Através desse atributo, podemos acessar as entradas passadas pelo usuário. Considere que o código acima 
# é o conteúdo de um arquivo chamado args.py. Se esse arquivo for executado da seguinte forma:

# Entrada de dados
# $ python args.py Hello world

# Produzirá a seguinte saída:

# args.py
# Hello
# world