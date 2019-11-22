
import random
import math
import numpy as np

class AlgoritmoGenetico:


    @staticmethod
    def gerar_populacao(qtd):

        populacao = []

        for x in range(8):
            populacao.append(AlgoritmoGenetico.gerar_individuo(qtd))
        return populacao


    @staticmethod
    def gerar_individuo(qtd):
        individuo = []
        while (True):
            rand = random.randint(1, qtd)
            if not (individuo.__contains__(rand)):
                individuo.append(rand)

            if len(individuo) == 6:
                break
        individuo.append(individuo[0])

        return individuo

    @staticmethod
    def calculateDistancias(populacao, cidades):

        distancias = []

        for indice, individuo in enumerate(populacao):

            distancia = 0

            for i in range(len(individuo)):
                cidadeOriggem = cidades[individuo[i] - 1]
                cidadeDestino = cidades[(individuo[(i + 1) % len(cidades)] - 1)]
                distancia += math.sqrt(((cidadeOriggem[0] - cidadeDestino[0]) ** 2) + ((cidadeOriggem[1] - cidadeDestino[1]) ** 2))

            distancias.append(distancia)
            # if distancia < menor_distancia:
            #     menor_distancia = distancia
            #     indice_menorDistancia = indice

        return distancias

    @staticmethod
    def calcularFitness(distancias, maior_distancia):

        vetor_fitness = []

        for indice, dist in enumerate(distancias):
            vetor_fitness.append(AlgoritmoGenetico.fitness(dist, indice, maior_distancia))

        return vetor_fitness

    @staticmethod
    def fitness(distancia, indice, k):

        y = (-1 / (k ** 2) * (distancia ** 2)) + 1


        return (round(y, 3), indice)

    @staticmethod
    def get_ranking(vetor_fitness):

        n = len(vetor_fitness)
        max_value = 10
        min_value = 0

        aptidoes = []

        for i in range(len(vetor_fitness)):
            f = (min_value + (max_value - min_value) * (len(vetor_fitness) - (i + 1))/(len(vetor_fitness) - 1))
            aptidoes.append((f, vetor_fitness[i][1]))

        return aptidoes


    @staticmethod
    def printArray(array):

        for i in array:
            print(i)
