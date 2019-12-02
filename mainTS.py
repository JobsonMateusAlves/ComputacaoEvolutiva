import random
from Geral import Geral

from Methods import Methods
import matplotlib.pyplot as plt

from plot import MyLine

from ReaderManager import ReaderManager

random.seed(1)

c = ReaderManager.get_data()
c.remove(c[0])
cidades = c
cidades = [(1, 1), (1, 3), (2, 3), (3, 2), (3, 4), (2, 5)]

populacao = []
# maior_distancia = 375674
maior_distancia = 400000
max_geracoes = 50
qtd_populacao = 50
k = 10

TAXA_CROSSOVER = 0.75
TAXA_MUTACAO = 0.1
menor = 1000000

CROSSOVER = 1  # ou 2
MUTACAO = 2  # ou 2