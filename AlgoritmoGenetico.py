# import random
# import math
# from Geral import Geral
#
# from Methods import Methods
#
#
# class AlgoritmoGenetico:
#
#     cidades = []
#     populacao = []
#     maior_distancia = 25
#     max_geracoes = 1
#     qtd_populacao = 8
#
#     distancias = []
#     probabilidades = []
#     selecionados = []
#     array_filhos = []
#     todos_individuos = []
#     nova_populacao = []
#
#
#     def __init__(self, cidades, maior_distancia, max_geracoes, qtd_populacao):
#
#         self.cidades = cidades
#         self.maior_distancia = maior_distancia
#         self.max_geracoes = max_geracoes
#         self.qtd_populacao = qtd_populacao
#
#     def life_cycle(self):
#
#         for i in range(self.max_geracoes):
#             print("{} - Geração".format(i))
#
#             self.gerar_populacao()
#
#             self.distancia()
#
#             self.fitness()
#
#             self.selecao_reproducao()
#
#             self.reproduzir()
#
#             self.mutacao()
#
#             self.merge_all_individuos()
#
#             self.selecionar()
#
#             self.reiniciar()
#
#
#     def gerar_populacao(self):
#         populacao = Methods.gerar_populacao(len(self.cidades), self.qtd_populacao)
#         Geral.printArray(populacao)
#
#     def distancia(self):
#         print("Distancias")
#         self.distancias = Methods.calculateDistancias(self.populacao, self.cidades)
#         Geral.printArray(self.distancias)
#
#     def fitness(self):
#         print("Fitness:")
#         vetor_fitness = Methods.calcularFitness(self.distancias, self.maior_distancia)
#         vetor_fitness.sort()
#         Geral.printArray(vetor_fitness)
#
#         print("Ranking")
#         aptidoes = Methods.get_ranking(vetor_fitness)
#         Geral.printArray(aptidoes)
#
#         print("Probabilidades")
#         soma = Methods.get_soma_aptidoes(aptidoes)
#         self.probabilidades = Methods.calcular_probabilidades(aptidoes, soma)
#         Geral.printArray(self.probabilidades)
#
#     def selecao_reproducao(self):
#
#         for index in range(int(self.qtd_populacao / 2)):
#             pos = []
#             pos.append(Methods.roleta(self.probabilidades))
#             pos.append(Methods.roleta(self.probabilidades))
#             self.selecionados.append(pos)
#
#     def reproduzir(self):
#         print("filhos")
#
#         for selecionado in self.selecionados:
#             pais = [self.populacao[selecionado[0]], self.populacao[selecionado[1]]]
#             filhos = Methods.reproduzir(pais, 1)
#             self.array_filhos.append(filhos[0])
#             self.array_filhos.append(filhos[1])
#         Geral.printArray(self.array_filhos)
#
#     def mutacao(self):
#
#         rand = random.randint(0, len(self.array_filhos) - 1)
#         Methods.mutacao(self.array_filhos[rand], 0)
#
#     def merge_all_individuos(self):
#
#         print("todos")
#         for individuo in self.populacao:
#             self.todos_individuos.append(individuo)
#         for filho in self.array_filhos:
#             self.todos_individuos.append(filho)
#
#     def selecionar(self):
#
#         self.todos_individuos.sort()
#         # Geral.printArray(self.todos_individuos)
#
#         print("selecionados")
#         for index in range(self.qtd_populacao):
#             self.nova_populacao.append(self.todos_individuos[index])
#         Geral.printArray(self.nova_populacao)
#
#     def reiniciar(self):
#         self.populacao = self.nova_populacao
#         self.distancias = []
#         self.probabilidades = []
#         self.selecionados = []
#         self.array_filhos = []
#         self.todos_individuos = []
#         self.nova_populacao = []
#
#
