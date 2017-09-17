# -*- coding: utf-8 -*-
from random import choice
class Board:
    def __init__(self, symbols):
        if len(symbols) != 8:
            raise ValueError('There must be exactly 8 symbols on the board')
        matrix = []
        symbols += symbols #se duplica la lista para que se repita dos veces cada simbolo
        for i in range(16):
            sym = choice(symbols)#se escoje al azar un simbolo de la lista y se mete en la matriz
            matrix.append(sym)
            symbols.remove(sym)
        self.matrix = matrix

    def __str__(self):
        separator = '-'*33 + '\n'
        between = '   |   '
        res = separator
        indx = 0
        for i in range(4):
            res += '|       '*4 + '|\n'
            res += '|   '
            for j in range(4):
                res += self.matrix[indx].encode('utf-8') + between
                indx += 1
            res += '\n' + '|       '*4 + '|'
            res += '\n' + separator
        return res

    def show(self, a, b):
        pass
