# modelos de acesso a arquivos com open()

# Modo de abertura de arquivos
# r - leitura
# w - escrita
# a - escrita no final do arquivo
# r+ - leitura e escrita
# w+ - leitura e escrita (cria o arquivo se não existir)
# a+ - leitura e escrita (abre o arquivo para escrita no final)

# teste de erros
busca = input('Digite o que deseja buscar: ')

try:
    manipulador = open('arquivo.txt', 'r',encoding='utf-8')
    for linha in manipulador:
        linha = linha.strip()
            if busca in linha:
                print("linha encontrada")
                print(linha)
            else:
                print('linha não encontrada')
except IOError:
    print('Arquivo não encontrado')
else:
    manipulador.close()
    print('Arquivo lido com sucesso')