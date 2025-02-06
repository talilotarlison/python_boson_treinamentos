def cal_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * cal_fatorial(n - 1)

# Exemplo de uso
if __name__ == "__main__":
    numero = int(input("Digite um número: "))
    print(f"O fatorial de {numero} é {cal_fatorial(numero)}")