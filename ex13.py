frase = "vamos aprender python na pratica"
# manipulação de strings
palavras = frase.split()
# interação com a lista
for letra in frase:
    print(letra)

pre = frase.find("python")
print(pre)

nome = "Python"
nome.lower()
nome.upper()
nome.capitalize()
nome.title()
nome.swapcase()
nome.islower()
nome.isupper()

frase_do_dia= "Hoje é um lindo dia"
nova_frase = frase_do_dia.replace("lindo", "maravilhoso")
print(nova_frase)
# limpar string com espaços
frase_input = "    hoje é um lindo dia    "
frase_input.strip()
frase_input.rstrip()
frase_input.lstrip()

frase_input.center(50, "*")
frase_input.ljust(50, "*")
frase_input.endswith("dia")
frase_input.startswith("hoje")

#docstrings
doc = """
uma documetação que pode ser acessada atraves do codido  e é muito util para documentar o codigo em varias linhas
"""

print(doc)