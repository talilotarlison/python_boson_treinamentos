# funcoes
def message_fixa():
    print("minha mensagem fixa")

message_fixa()

def soma(a, b):
    return a + b

def message(msg):
    print(msg)

def subtracao(a, b):
    return a - b

def quadrado(val):
    quadrado = []
    for x in val:
        quadrado.append(x * 2)
    return quadrado

if __name__ == "__main__":
    message("minha mensagem variavel")
    print(soma(10, 20))
    print(subtracao(10, 20))

    a = 10; b = 20
    print(a + b)
    print(soma(a + b))