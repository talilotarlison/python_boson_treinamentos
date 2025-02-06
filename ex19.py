#tratamento de erros
# try except else

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

#r = raund(n1/n2, 2)
try:
    r = round(n1/n2, 2)
except ZeroDivisionError:
    print('Divisão por zero não permitida')
    r = None
else:
    print(r)

