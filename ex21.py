#tratamento de erros
# try except else

def div(n1, n2):
    return round(n1/n2, 2)

## trantando erros de entrada
while True:
    try:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        break
    except ValueError:
        print('Erro ao ler o valor. Digite novamente')

try:
    r = div(n1, n2)
except ZeroDivisionError:
    print('Divisão por zero não permitida')
    r = None
except:
    print('Erro desconhecido')
    r = None
else:
    print(r)
finally:
    print('Executando o finally')

