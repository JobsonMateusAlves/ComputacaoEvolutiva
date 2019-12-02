import random
from Geral import Geral
import math

from Methods import Methods
import matplotlib.pyplot as plt

from plot import MyLine

from ReaderManager import ReaderManager
#5
# random.seed(5)

c = ReaderManager.get_data()
c.remove(c[0])
cidades = c


populacao = []
maior_distancia = 25
max_geracoes = 50
qtd_populacao = 1

k = 10
# ----------------------------------------------- Inicio ---------------------------------
T = 1000
B = 0.99
Tmin = 1
# cidades = [(1, 1), (1, 3), (2, 3), (3, 2), (3, 4), (2, 5)]

populacao = Methods.gerar_populacao(len(cidades), qtd_populacao)
Geral.printArray(populacao)

distancia1 = Methods.calculateDistancias(populacao, cidades)[0]
contador = 0
while T >= Tmin:
    contador += 1
    print(T)
    print(contador)
    for i in range(k):
        nova_populacao = [populacao[0].copy()]
        random.shuffle(nova_populacao[0])
        Geral.printArray(nova_populacao)

        distancia2 = Methods.calculateDistancias(nova_populacao, cidades)[0]

        if distancia2 < distancia1:
            populacao = nova_populacao
            break
        elif float(random.randint(0, 100))/100 < math.exp((distancia1 - distancia2)/T):
            populacao = nova_populacao
            break
    T = B * T

print(T)
print(contador)
fig, ax = plt.subplots()

for i in range(len(cidades)):
    m = 'o'
    plt.scatter(cidades[i][0], cidades[i][1], marker=m)

x = []
y = []
for i in populacao[0]:
    x.append(cidades[i - 1][0])
    y.append(cidades[i - 1][1])
line = MyLine(x, y, mfc='red', ms=12)
ax.add_line(line)

plt.show()





