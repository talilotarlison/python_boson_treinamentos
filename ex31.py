# modelos de acesso a arquivos com open()

# Modo de abertura de arquivos
# r - leitura
# w - escrita
# a - escrita no final do arquivo
# r+ - leitura e escrita
# w+ - leitura e escrita (cria o arquivo se não existir)
# a+ - leitura e escrita (abre o arquivo para escrita no final)

# teste de erros
try:
    manipulador = open('arquivo.txt', 'w',encoding='utf-8')
    manipulador.write('Python é uma linguagem de programação\n')
    manipulador.write('Python é uma linguagem de programação\n')
except IOError:
    print('Arquivo não encontrado, nao foi possivel escrever')
else:
    manipulador.close()
    print('Arquivo escrito com sucesso')