import random
import math
from Geral import Geral

from AlgoritmoGenetico import AlgoritmoGenetico

cidades = [(1, 1), (1, 3), (2, 3), (3, 2), (3, 4), (2, 5)]
populacao = []
maior_distancia = 25
max_geracoes = 50
qtd_populacao = 8


print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("População")
populacao = AlgoritmoGenetico.gerar_populacao(len(cidades), qtd_populacao)
Geral.printArray(populacao)

for i in range(max_geracoes):
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("{} - Geração".format(i))
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Distancias")
    distancias = AlgoritmoGenetico.calculateDistancias(populacao, cidades)
    Geral.printArray(distancias)

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Fitness:")
    vetor_fitness = AlgoritmoGenetico.calcularFitness(distancias, maior_distancia)
    vetor_fitness.sort()
    Geral.printArray(vetor_fitness)

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Ranking")
    aptidoes = AlgoritmoGenetico.get_ranking(vetor_fitness)
    Geral.printArray(aptidoes)

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Probabilidades")
    soma = AlgoritmoGenetico.get_soma_aptidoes(aptidoes)
    probabilidades = AlgoritmoGenetico.calcular_probabilidades(aptidoes, soma)
    Geral.printArray(probabilidades)

    selecionados = []
    for index in range(int(qtd_populacao/2)):
        pos = []
        pos.append(AlgoritmoGenetico.roleta(probabilidades))
        pos.append(AlgoritmoGenetico.roleta(probabilidades))
        selecionados.append(pos)

    array_filhos = []
    for selecionado in selecionados:
        pais = [populacao[selecionado[0]], populacao[selecionado[1]]]
        filhos = AlgoritmoGenetico.reproduzir(pais, 1)
        array_filhos.append(filhos[0])
        array_filhos.append(filhos[1])

    print("filhos")
    Geral.printArray(array_filhos)








