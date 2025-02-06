# modelos de acesso a arquivos com open()

# Modo de abertura de arquivos
# r - leitura
# w - escrita
# a - escrita no final do arquivo
# r+ - leitura e escrita
# w+ - leitura e escrita (cria o arquivo se não existir)
# a+ - leitura e escrita (abre o arquivo para escrita no final)

# ler o arquivo
manipulador = open('arquivo.txt', 'r',encoding='utf-8')
conteudo = manipulador.read()
print(conteudo)
conteudo = manipulador.readeline()
conteudo = manipulador.readelines()
manipulador.close()

# teste de erros
try:
    manipulador = open('arquivo.txt', 'r',encoding='utf-8')
    for linha in manipulador:
        linha = linha.strip()
        print(linha)
except IOError:
    print('Arquivo não encontrado')
else:
    manipulador.close()
    print('Arquivo lido com sucesso')

# escrever no arquivo
manipulador = open('arquivo.txt', 'w')
manipulador.write('Python é uma linguagem de programação')
manipulador.close()