import random
import math

cidades = [(1, 1), (1, 3), (2, 3), (3, 2), (3, 4), (2, 5)]
populacao = []
maiorDistancia = 25

def gerar_populacao():

    for x in range(32):
        populacao.append(gerar_individuo())

def gerar_individuo():
    individuo = []
    while (True):
        rand = random.randint(1, 6)
        if not (individuo.__contains__(rand)):
            individuo.append(rand)

        if len(individuo) == 6:
            break
    individuo.append(individuo[0])
    print(individuo)
    return individuo

def fitness(distancia, indice, k):

    y = (-1/(k ** 2) * (distancia ** 2)) + 1

    return (y, indice)




gerar_populacao()

distancias = []
menor_distancia = 10000
indice_menorDistancia = -1

for indice, individuo in enumerate(populacao):

    distancia = 0

    for i in range(len(individuo)):
        cidadeOriggem = cidades[individuo[i] - 1]
        cidadeDestino = cidades[(individuo[(i + 1) % len(cidades)] - 1)]
        distancia += math.sqrt( ( (cidadeOriggem[0] - cidadeDestino[0]) ** 2 ) + ( (cidadeOriggem[1] - cidadeDestino[1]) ** 2 ) )

    distancias.append(distancia)
    if distancia < menor_distancia:
        menor_distancia = distancia
        indice_menorDistancia = indice

print("------------------------------------------")
print(distancias)
# print(indice_menorDistancia)
# print(menor_distancia)
# print(populacao[indice_menorDistancia])
print("------------------------------------------")

vetor_fitness = []

for indice, dist in enumerate(distancias):
    vetor_fitness.append(fitness(dist, indice, maiorDistancia))

vetor_fitness.sort()
print(vetor_fitness)

aux = vetor_fitness.copy()

melhores = []
for i in range(8):

    melhores.append(aux[len(aux) - 1])
    aux.remove(aux[len(aux) - 1])

piores = []
for i in range(8):
    piores.append(aux[0])
    aux.remove(aux[0])

print(melhores)
print(piores)






