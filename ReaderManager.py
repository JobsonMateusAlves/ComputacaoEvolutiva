import math
import numpy as np

DATASET = './ncit30.dat'

class ReaderManager:

    @staticmethod
    def get_data():
        file = DATASET
        data = []
        with open(file) as f:
            conteudo = f.readlines()
        lines = [line.strip() for line in conteudo]

        for i in range(len(lines)):
            data.append([])
            vetor = lines[i].split()
            for pos in vetor:
                data[i].append(int(pos))

        return data

    # @staticmethod
    # def get_respostas():
    #     file = RESPOSTAS
    #     respostas = []
    #     with open(file) as f:
    #         conteudo = f.readlines()
    #     lines = [line.strip() for line in conteudo]
    #
    #     for i in range(len(lines)):
    #         respostas.append([])
    #         vetor = lines[i].split()
    #         for pos in vetor:
    #             respostas[i].append(float(pos))
    #
    #     return respostas
    #
    # @staticmethod
    # def get_entradas_teste(num):
    #     if num == 2:
    #         file = TESTE_2
    #     elif num == 5:
    #         file = TESTE_5
    #     else:
    #         file = TESTE_10
    #
    #     entradas = []
    #     with open(file) as f:
    #         conteudo = f.readlines()
    #     lines = [line.strip() for line in conteudo]
    #
    #     for i in range(len(lines)):
    #         entradas.append([])
    #         vetor = lines[i].split()
    #         for pos in vetor:
    #             entradas[i].append(float(pos))
    #
    #     return entradas
    #
    # @staticmethod
    # def get_entradas_xor():
    #     file = XOR_X
    #     entradas = []
    #     with open(file) as f:
    #         conteudo = f.readlines()
    #     lines = [line.strip() for line in conteudo]
    #
    #     for i in range(len(lines)):
    #         entradas.append([])
    #         vetor = lines[i].split()
    #         for pos in vetor:
    #             entradas[i].append(float(pos))
    #
    #     return entradas
    #
    # @staticmethod
    # def get_respostas_xor():
    #     file = XOR_D
    #     respostas = []
    #     with open(file) as f:
    #         conteudo = f.readlines()
    #     lines = [line.strip() for line in conteudo]
    #
    #     for i in range(len(lines)):
    #         respostas.append([])
    #         vetor = lines[i].split()
    #         for pos in vetor:
    #             respostas[i].append(float(pos))
    #
    #     return respostas
