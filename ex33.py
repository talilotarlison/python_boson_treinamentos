import matplotlib.pyplot as plt
# import numpy as np

tempo_horas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperatura = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# grafico de dispersão
plt.scatter(tempo_horas, temperatura)
plt.xlabel('Tempo (horas)')
plt.ylabel('Temperatura (C)')
plt.title('Variação da temperatura ao longo do tempo')
plt.show()

# grafico de barras
plt.bar(tempo_horas, temperatura)
plt.xlabel('Tempo (horas)')
plt.ylabel('Temperatura (C)')
plt.title('Variação da temperatura ao longo do tempo')

plt.xticks(range(0,max(tempo)+1,2))
plt.show()

# grafico de linha
plt.plot(tempo_horas, temperatura)
plt.xlabel('Tempo (horas)')
plt.ylabel('Temperatura (C)')
plt.title('Variação da temperatura ao longo do tempo')
plt.show()
