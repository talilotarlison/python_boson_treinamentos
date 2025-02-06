import os 
# renomear arquivos de um diretório com python
os.chdir("C:\\Teste")
print("Diretorio: ", os.getcwd())

padrao_nome = input("Digite o padrão do nome do arquivo: ")

for contador, arquivo in enumerate(os.listdir()):
    if os.path.isfile(arquivo):
         nome_arq, extensao = os.path.splitext(arquivo)
         nome_arq = padrao_nome + ' ' + str(contador)

         novo_nome = f'{nome_arq}{extensao}'
         os.rename(arquivo, novo_nome)
         
print("Arquivos renomeados com sucesso!")