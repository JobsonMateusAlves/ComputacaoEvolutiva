import random
from Geral import Geral
import math

from Methods import Methods
import matplotlib.pyplot as plt

from plot import MyLine

from ReaderManager import ReaderManager
#5
random.seed(5)

c = ReaderManager.get_data()
c.remove(c[0])
cidades = c


populacao = []
max_geracoes = 50
qtd_populacao = 1

T = 1000
k = 10
T = 1000
B = 0.99
Tmin = 1
MUTACAO = 1
taxa_mutacao = 0.1
execuoes = 5
# cidades = [(1, 1), (1, 3), (2, 3), (3, 2), (3, 4), (2, 5)]

for exec in range(execuoes):
    print("Exec: {} -------------------------------------".format())
    for i in range(2):
        T = 1000

        if i == 0:
            MUTACAO = 1
        else:
            MUTACAO = 2

        populacao = Methods.gerar_populacao(len(cidades), qtd_populacao)
        # Geral.printArray(populacao)

        distancia1 = Methods.calculateDistancias(populacao, cidades)[0]
        while T >= Tmin:
            for i in range(k):
                nova_populacao = [populacao[0].copy()]
                Methods.mutacao(nova_populacao[0], MUTACAO, taxa_mutacao)

                distancia2 = Methods.calculateDistancias(nova_populacao, cidades)[0]

                if distancia2 < distancia1:
                    populacao = nova_populacao
                    break
                elif float(random.randint(0, 100))/100 < math.exp((distancia1 - distancia2)/T):
                    populacao = nova_populacao
                    break
            T = B * T

        print(populacao[0])
        print("Temperatura final: {}".format(T))
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





