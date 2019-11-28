import random
import math
from Geral import Geral

from AlgoritmoGenetico import AlgoritmoGenetico

cidades = [(1, 1), (1, 3), (2, 3), (3, 2), (3, 4), (2, 5), (5, 2), (9, 0), (7, 5), (0, 3), (1, 9)]
populacao = []
maior_distancia = 25
max_geracoes = 1
qtd_populacao = 8


print("População")
populacao = AlgoritmoGenetico.gerar_populacao(len(cidades), qtd_populacao)
Geral.printArray(populacao)

for i in range(max_geracoes):
    print("{} - Geração".format(i))

    #Distancias
    print("Distancias")
    distancias = AlgoritmoGenetico.calculateDistancias(populacao, cidades)
    Geral.printArray(distancias)

    # Fitness
    print("Fitness:")
    vetor_fitness = AlgoritmoGenetico.calcularFitness(distancias, maior_distancia)
    vetor_fitness.sort()
    Geral.printArray(vetor_fitness)

    # Ranking
    print("Ranking")
    aptidoes = AlgoritmoGenetico.get_ranking(vetor_fitness)
    Geral.printArray(aptidoes)

    # Probabilidades
    print("Probabilidades")
    soma = AlgoritmoGenetico.get_soma_aptidoes(aptidoes)
    probabilidades = AlgoritmoGenetico.calcular_probabilidades(aptidoes, soma)
    Geral.printArray(probabilidades)

    # Roleta
    selecionados = []
    for index in range(int(qtd_populacao/2)):
        pos = []
        pos.append(AlgoritmoGenetico.roleta(probabilidades))
        pos.append(AlgoritmoGenetico.roleta(probabilidades))
        selecionados.append(pos)
    # Reprodução
    print("filhos")
    array_filhos = []
    for selecionado in selecionados:
        pais = [populacao[selecionado[0]], populacao[selecionado[1]]]
        filhos = AlgoritmoGenetico.reproduzir(pais, 1)
        array_filhos.append(filhos[0])
        array_filhos.append(filhos[1])
    Geral.printArray(array_filhos)

    # Mutação


    print("todos")
    todos_individuos = []
    for individuo in populacao:
        todos_individuos.append(individuo)
    for filho in array_filhos:
        todos_individuos.append(filho)
    todos_individuos.sort()
    Geral.printArray(todos_individuos)

    nova_populacao = []

    for index in range(qtd_populacao):
        nova_populacao.append(todos_individuos[index])

    print("selecionados")
    Geral.printArray(nova_populacao)

    print("dashdakas")
    print("")

    # AlgoritmoGenetico.scramble(nova_populacao[0])
