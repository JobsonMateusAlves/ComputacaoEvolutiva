import random
import math
from AlgoritmoGenetico import AlgoritmoGenetico

cidades = [(1, 1), (1, 3), (2, 3), (3, 2), (3, 4), (2, 5)]
populacao = []
maior_distancia = 25
max_geracoes = 50


print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("População")
populacao = AlgoritmoGenetico.gerar_populacao(len(cidades))
AlgoritmoGenetico.printArray(populacao)

for i in range(max_geracoes):
    print("{} - Geração".format(i))
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Distancias")
    distancias = AlgoritmoGenetico.calculateDistancias(populacao, cidades)
    AlgoritmoGenetico.printArray(distancias)

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Fitness:")
    vetor_fitness = AlgoritmoGenetico.calcularFitness(distancias, maior_distancia)
    vetor_fitness.sort()
    AlgoritmoGenetico.printArray(vetor_fitness)

    print("Min")
    AlgoritmoGenetico.printArray(AlgoritmoGenetico.get_ranking(vetor_fitness))









