#typecasting
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

soma = valor1 + valor2
print(f"A soma dos valores é: {soma}")

def soma(a, b):
    return a + b

print(f"A soma dos valores é: {soma(valor1, valor2)}")