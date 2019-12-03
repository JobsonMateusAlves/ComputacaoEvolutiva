import random
from Geral import Geral
from datetime import datetime
from Methods import Methods
import matplotlib.pyplot as plt
import numpy as np

from plot import MyLine

from ReaderManager import ReaderManager

c = ReaderManager.get_data()
c.remove(c[0])
cidades = c
cidades = [(1, 1), (1, 3), (2, 3), (3, 2), (3, 4), (2, 5)]

valor_medio_melhores = []
geracao_x_fitness = []

populacao = []

max_geracoes = 50
qtd_populacao = 4

TAXA_CROSSOVER = 0.75
TAXA_MUTACAO = 0.1
menor = 1000000000000

CROSSOVER = 1
MUTACAO = 1

for m in range(5):
    geracao_x_fitness.append([])
    tempos = []
    melhores = []
    iteracoes = []
    random.seed(m + 1)

    print("---------------------------- Execução: {} ---------------------------------".format(m + 1))

    for n in range(4):
        geracao_x_fitness[m].append([])
        menor = 1000000000000

        now = datetime.now()
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

        for i in range(max_geracoes):

            # ------------------------------------------------- DISTANCIA -----------------------------------------------------
            distancias = Methods.calculateDistancias(populacao, cidades)


            # -------------------------------------------------- FITNESS -----------------------------------------------------
            vetor_fitness = []
            for index_distancia, distancia in enumerate(distancias):
                vetor_fitness.append((round(distancia, 3), index_distancia))
            vetor_fitness.sort()

            # -------------------------------------------------- RANKING -----------------------------------------------------
            aptidoes = Methods.get_ranking(vetor_fitness)

            # ----------------------------------------------- PROBABILIDADES -----------------------------------------------------
            soma = Methods.get_soma_aptidoes(aptidoes)
            probabilidades = Methods.calcular_probabilidades(aptidoes, soma)

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

            # -------------------------------------------- DISTANCIA E FITNESS -------------------------------------------------
            distancias = Methods.calculateDistancias(todos_individuos, cidades)
            if min(distancias) < menor:
                menor = min(distancias)
            vetor_fitness = []
            for index_distancia, distancia in enumerate(distancias):
                vetor_fitness.append((distancia, index_distancia))
            vetor_fitness.sort()

            # ----------------------------------------------- NOVA POPULACAO -------------------------------------------------
            nova_populacao = []
            for index in range(qtd_populacao):
                nova_populacao.append(todos_individuos[vetor_fitness[index][1]])

            # ------------------------------------------------- REINICIANDO -------------------------------------------------
            populacao = nova_populacao
            geracao_x_fitness[m][n].append(vetor_fitness[0][0])
            distancias = []
            probabilidades = []
            selecionados = []
            array_filhos = []
            todos_individuos = []
            nova_populacao = []

        # ------------------------------------------------- Prints -------------------------------------------------------

        rota = Methods.calculateDistancias([populacao[0]], cidades)[0]
        print("Melhor rota: {}".format(rota))
        print(populacao[0])
        # print("Menor: {}".format(menor))

        melhores.append(Methods.calculateDistancias([populacao[0]], cidades)[0])

        # ------------------------------------------------- Plot -------------------------------------------------------
        plt.rcParams.update({'figure.max_open_warning': 0})
        fig, ax = plt.subplots()

        for i in range(len(cidades)):
            q = 'o'
            plt.scatter(cidades[i][0], cidades[i][1], marker=q)

        x = []
        y = []
        for i in populacao[0]:
            x.append(cidades[i - 1][0])
            y.append(cidades[i - 1][1])
        line = MyLine(x, y, mfc='red', ms=12)
        ax.add_line(line)

        now2 = datetime.now()
        # print("1: {} / 2: {}".format(now, now2))
        tempos.append(now2 - now)
    # ------------------------------------------------- Prints2 -------------------------------------------------------
    print("")
    print("Tempo medio: {}".format(np.sum(tempos)/4))
    print("Valor medio das melhores: {}".format(np.sum(melhores)/4))
    valor_medio_melhores.append(np.sum(melhores)/4)

    # ----------------------------------- ger_x_fit ---------------------------------

    maior = 0
    index_maior = 0
    for il, l in enumerate(geracao_x_fitness[m]):
        if l[len(l) - 1] > maior:
            maior = l[len(l) - 1]
            index_maior = il


    fig2, ax2 = plt.subplots()

    ger = []
    fit = []
    for g, g_x_f in enumerate(geracao_x_fitness[m][index_maior]):
        ger.append(g)
        fit.append(g_x_f)
    line2 = MyLine(ger, fit, mfc='red', ms=12)
    ax2.add_line(line2)

    ax2.set_xlim([0, 50])
    if len(cidades) == 30:
        ax2.set_ylim([min(valor_medio_melhores) - 40000, max(valor_medio_melhores) + 50000])
    else:
        ax2.set_ylim(0,  25)
plt.show()
