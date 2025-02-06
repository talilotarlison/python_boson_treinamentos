bebidas = []

def show_bebidas_order(bebidas):
    sorted(bebidas,reverse=True)    
    for bebida in bebidas:
        print(bebida)

for i in range(5):
    bebida = input("Qual a bebida adicinar: ")
    bebidas.append(bebida)
#https://docs.python.org/pt-br/dev/howto/sorting.html
show_bebidas_order(bebidas)