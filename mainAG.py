import random
from Geral import Geral
from datetime import datetime
from Methods import Methods
import matplotlib.pyplot as plt

from plot import MyLine

from ReaderManager import ReaderManager

random.seed(3)

c = ReaderManager.get_data()
c.remove(c[0])
cidades = c
# cidades = [(1, 1), (1, 3), (2, 3), (3, 2), (3, 4), (2, 5)]


populacao = []
maior_distancia = 375674
maior_distancia = 25
max_geracoes = 10000
qtd_populacao = 50

TAXA_CROSSOVER = 0.75
TAXA_MUTACAO = 0.1
menor = 1000000000000

CROSSOVER = 1  # ou 2
MUTACAO = 1  # ou 2

now = datetime.now()
hr = now.strftime("%H:%M:%S")
print(hr)
# for m in range(5):
for n in range(4):

    menor = 100000000

    if n == 0:
        CROSSOVER = 1
        MUTACAO = 1
    elif n == 1:
        CROSSOVER = 1
        MUTACAO = 2
    elif n == 2:
        CROSSOVER = 2
        MUTACAO = 1
    else:
        CROSSOVER = 2
        MUTACAO = 2

    populacao = Methods.gerar_populacao(len(cidades), qtd_populacao)
    # print("População")
    # Geral.printArray(populacao)

    for i in range(max_geracoes):
        # print("{} - Geração".format(i + 1))

        # ------------------------------------------------- DISTANCIA -----------------------------------------------------
        distancias = Methods.calculateDistancias(populacao, cidades)
        # print("------------------------------------------------- DISTANCIA -----------------------------------------------------")
        # Geral.printArray(distancias)

        # -------------------------------------------------- FITNESS -----------------------------------------------------
        vetor_fitness = Methods.calcularFitness(distancias, maior_distancia)
        vetor_fitness.sort(reverse=True)
        # print("-------------------------------------------------- FITNESS -----------------------------------------------------")
        # Geral.printArray(vetor_fitness)

        # -------------------------------------------------- RANKING -----------------------------------------------------
        aptidoes = Methods.get_ranking(vetor_fitness)
        # print("-------------------------------------------------- RANKING -----------------------------------------------------")
        # Geral.printArray(aptidoes)

        # ----------------------------------------------- PROBABILIDADES -----------------------------------------------------
        soma = Methods.get_soma_aptidoes(aptidoes)
        probabilidades = Methods.calcular_probabilidades(aptidoes, soma)
        # print("----------------------------------------------- PROBABILIDADES -----------------------------------------------------")
        # Geral.printArray(probabilidades)

        # -------------------------------------------------- ROLETA -----------------------------------------------------
        selecionados = []
        for index in range(int(qtd_populacao/2)):
            pos = []
            pos.append(Methods.roleta(probabilidades))
            pos.append(Methods.roleta(probabilidades))
            selecionados.append(pos)

        # ------------------------------------------------ REPRODUCAO -----------------------------------------------------
        array_filhos = []
        for selecionado in selecionados:
            pais = [populacao[selecionado[0]], populacao[selecionado[1]]]
            filhos = Methods.reproduzir(pais, CROSSOVER, TAXA_CROSSOVER)
            if len(filhos) != 0:
                array_filhos.append(filhos[0])
                array_filhos.append(filhos[1])

        # -------------------------------------------------- MUTACAO -----------------------------------------------------
        for i, ind in enumerate(array_filhos):
            array_filhos[i] = Methods.mutacao(ind, MUTACAO, TAXA_MUTACAO)

        # --------------------------------------------------- MERGE ------------------------------------------------------
        todos_individuos = []
        for individuo in populacao:
            todos_individuos.append(individuo)
        for filho in array_filhos:
            todos_individuos.append(filho)
        # print("----------------------------------------------- TODOS -----------------------------------------------------")
        # Geral.printArray(todos_individuos)

        # -------------------------------------------- DISTANCIA E FITNESS -------------------------------------------------
        distancias = Methods.calculateDistancias(todos_individuos, cidades)
        if min(distancias) < menor:
            menor = min(distancias)
        vetor_fitness = Methods.calcularFitness(distancias, maior_distancia)
        vetor_fitness.sort(reverse=True)
        # print("----------------------------------------------- FITNESS_TODOS -----------------------------------------------------")
        # Geral.printArray(vetor_fitness)

        # ----------------------------------------------- NOVA POPULACAO -------------------------------------------------
        nova_populacao = []
        for index in range(qtd_populacao):
            nova_populacao.append(todos_individuos[vetor_fitness[index][1]])
        # print("----------------------------------------------- SELECIONADOS -----------------------------------------------------")
        # Geral.printArray(nova_populacao)

        # ------------------------------------------------- REINICIANDO -------------------------------------------------
        populacao = nova_populacao
        distancias = []
        probabilidades = []
        selecionados = []
        array_filhos = []
        todos_individuos = []
        nova_populacao = []

    print("Melhor")
    print(populacao[0])
    print("Menor: {}".format(menor))
    print("Selecionado: {}".format(Methods.calculateDistancias([populacao[0]], cidades)[0]))


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

now = datetime.now()
hr = now.strftime("%H:%M:%S")
print(hr)

plt.show()


