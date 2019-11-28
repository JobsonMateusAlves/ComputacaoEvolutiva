
import random
import math
import numpy as np
from Geral import Geral

class Methods:

#-------------------------------------------------- Gerar Populacao --------------------------------------------------
    @staticmethod
    def gerar_populacao(qtd, qtd_populacao):

        populacao = []

        for x in range(qtd_populacao):
            populacao.append(Methods.gerar_individuo(qtd))
        return populacao


    @staticmethod
    def gerar_individuo(qtd):
        individuo = []
        while (True):
            rand = random.randint(1, qtd)
            if not (individuo.__contains__(rand)):
                individuo.append(rand)

            if len(individuo) == qtd:
                break

        return individuo

#----------------------------------------------- Calcular Distancia --------------------------------------------------

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

#----------------------------------------------- Fitness --------------------------------------------------
    @staticmethod
    def calcularFitness(distancias, maior_distancia):

        vetor_fitness = []

        for indice, dist in enumerate(distancias):
            vetor_fitness.append(Methods.fitness(dist, indice, maior_distancia))

        return vetor_fitness

    @staticmethod
    def fitness(distancia, indice, k):

        y = (-1 / (k ** 2) * (distancia ** 2)) + 1


        return (round(y, 3), indice)

    @staticmethod
    def get_ranking(vetor_fitness):

        n = len(vetor_fitness)
        max_value = len(vetor_fitness)
        min_value = 0

        aptidoes = []

        for i in range(len(vetor_fitness)):
            f = (min_value + (max_value - min_value) * (len(vetor_fitness) - (i + 1))/(len(vetor_fitness) - 1))
            aptidoes.append((f, vetor_fitness[i][0], vetor_fitness[i][1]))

        return aptidoes

    @staticmethod
    def get_soma_aptidoes(array):
        soma = 0
        for p in array:
            soma += p[0]

        return soma

    @staticmethod
    def calcular_probabilidades(array, soma):

        probabilidades = []
        for p in array:
            probabilidades.append((round(p[0]/soma, 3), p[1], p[2]))

        return probabilidades

#----------------------------------------- Seleção para reprodução -------------------------------------------
    @staticmethod
    def roleta(array):

        population = []
        weights = []

        for p in array:
            population.append(p[2])
            weights.append(p[0])

        result = random.choices(
            population=population,
            weights=weights,
            k=100
        )


        return result[random.randint(0, 99)]

#----------------------------------------------- Crossover --------------------------------------------------
    @staticmethod
    def reproduzir(individuos, operador):

        if operador == 0:
            return Methods.cross_over_pbx(individuos)
        else:
            return Methods.cross_over_cx(individuos)


    @staticmethod
    def cross_over_pbx(individuos):
        print("pbx")

        filhos = []
        posicoes = []
        contador = 0
        while(contador != 3):
            pos = random.randint(0, len(individuos[0]) - 1)
            if not posicoes.__contains__(pos):
                posicoes.append(pos)
                contador += 1

        for i in range(2):
            filho = []
            fixos = []
            for p in posicoes:
                fixos = [individuos[i][p], individuos[i][p], individuos[i][p]]

            for j in range(len(individuos[i])):
                if posicoes.__contains__(j):
                    filho.append(individuos[i][j])
                else:
                    for k in individuos[(i + 1) % 2]:
                        if not fixos.__contains__(k) and not filho.__contains__(k):
                            filho.append(k)
                            break
            filhos.append(filho)

        return filhos

    @staticmethod
    def cross_over_cx(individuos):
        print("cx")

        filhos = []
        first = random.randint(0, len(individuos[0]) - 1)
        posicoes1 = [first]

        last_pos = first

        current2 = individuos[1][last_pos]

        last_pos = Geral.busca(individuos[0], current2)

        while(not posicoes1.__contains__(last_pos)):

            posicoes1.append(last_pos)

            current2 = individuos[1][last_pos]

            last_pos = Geral.busca(individuos[0], current2)

        if len(posicoes1) == len(individuos[0]):

            for i in range(len(individuos)):
                filho = []
                for p in posicoes1:
                    filho.append(individuos[i][p])

                filhos.append(filho)
        else:

            for i in range(len(individuos)):
                filho = []
                for j in range(len(individuos[0])):

                    if posicoes1.__contains__(j):
                        filho.append(individuos[i][j])
                    else:
                        filho.append(individuos[(i + 1) % 2][j])

                filhos.append(filho)

        return filhos

#----------------------------------------------- Mutacao --------------------------------------------------
    @staticmethod
    def mutacao(individuo, operador):

        if operador == 0:
            return Methods.scramble(individuo)
        else:
            return Methods.order_based(individuo)


    @staticmethod
    def scramble(individuo):


        inicial = random.randint(0, len(individuo) - 2)

        final = random.randint(inicial + 1, len(individuo) - 1)

        print("inicial: {} Final: {}".format(inicial, final))

        array = []

        for index, gene in enumerate(individuo):
            if index >= inicial and index <= final:
                array.append(gene)

        random.shuffle(array)

        contador = 0
        for index in range(len(individuo)):
            if index >= inicial and index <= final:
                individuo[index] = array[contador]
                contador += 1

        return individuo


    @staticmethod
    def order_based(individuo):
        primeiro = random.randint(0, len(individuo) - 1)
        segundo  = primeiro
        while (segundo == primeiro):
            segundo = random.randint(0, len(individuo) - 1)

        aux = individuo[primeiro]

        individuo[primeiro] = individuo[segundo]
        individuo[segundo] = aux

        return individuo