

class Geral:

    @staticmethod
    def printArray(array):

        for i in array:
            print(i)

    @staticmethod
    def busca(array, value):

        for pos in range(len(array)):

            if array[pos] == value:
                return pos

        return -1