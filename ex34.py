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
