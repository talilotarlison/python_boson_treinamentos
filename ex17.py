def contar(num=12, carcter='*'):
    for i in range(num):
        print(carcter)

def soma_multipla(a,b,c=0):
    if (c==0):
        return a+b
    else:
        return a+b+c


if __name__ == '__main__':
    contar(5, '!')
    contar(num=12, carcter='*')