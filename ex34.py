import pandas as pd
import matplotlib.pyplot as plt

# Inicializar os arrays
notas = []
nome_alunos = []
nivel = []

# Abrir o arquivo CSV e preencher os arrays
df = pd.read_csv('notas.csv')

for index, row in df.iterrows():
    nome_alunos.append(row['nome_aluno'])
    notas.append(row['nota'])
    nivel.append(row['nivel'])

# Exibir as listas preenchidas para verificar
print("Alunos:", nome_alunos)
print("Notas:", notas)
print("Níveis:", nivel)

# Gráfico de barras: Eixo X = Alunos, Eixo Y = Notas
plt.figure(figsize=(10, 6))
plt.bar(nome_alunos, notas, color='skyblue')

# Adicionar título e rótulos aos eixos
plt.title('Notas dos Alunos', fontsize=14)
plt.xlabel('Alunos', fontsize=12)
plt.ylabel('Notas', fontsize=12)

# Adicionar as legendas
plt.xticks(rotation=45, ha='right')  # Girar as legendas dos alunos para melhorar a legibilidade
plt.tight_layout()  # Ajustar o layout para que os rótulos não saiam da tela

# Exibir o gráfico
plt.show()


# calculo media aritimedica
soma_notas = sum(notas)
media_aritmetica = soma_notas / len(notas)
print("Média Aritmética:", media_aritmetica)

# menor nota entre alunos
menor_nota = min(notas)

for aluno in notas:
    if menor_nota == aluno:
        n = notas.index(aluno)
        nome_aluno_menor_nota = nome_alunos[n]
        print(nome_aluno_menor_nota)
        break

print("Menor Nota:", menor_nota, nome_aluno_menor_nota)

# maior nota entre alunos
maior_nota = max(notas)
nome_aluno_maior_nota = nome_alunos[notas.index(maior_nota)]
print(nome_aluno_maior_nota)
print("Maior Nota:", maior_nota,nome_aluno_maior_nota)


# calculo moda das notas
from statistics import multimode
moda_notas = multimode(notas)
print("Moda das Notas:", moda_notas)

array_numeros = [3,9,1,9,7,8,10,4,5,4]
moda_array = multimode(array_numeros)
print("Moda do Array de Numeros:", moda_array)


