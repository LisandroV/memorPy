# -*- coding: utf-8 -*-
from random import choice

positions = list('abcdefghijklmnop') #lisata de las posiciones de las cartas

#transforma la lista de elementos del memorama en un tablero en cadena
def stringifyBoardList(elem_list):
    separator = '-'*33 + '\n'
    between = '   |   '
    res = separator
    indx = 0
    for i in range(4):
        tmp = '|   '
        for j in range(4):
            res += '|' + positions[indx] + '      '
            tmp += elem_list[indx].encode('utf-8') + between
            indx += 1
        res += '|\n' + tmp + '\n' + '|       '*4 + '|'
        res += '\n' + separator
    return res

#esta funcion regresa aleatoriamente todos los simbolos que se necesitan para el memorama
def takeRandomSymbols(sym_list):
    matrix = []
    symbols = sym_list*2 #se duplica la lista para que se repita dos veces cada simbolo
    for i in range(16):
        sym = choice(symbols)#se escoje al azar un simbolo de la lista y se mete en la matriz
        matrix.append(sym)
        symbols.remove(sym)
    return matrix


class Board:
    def __init__(self, symbols):
        if len(symbols) != 8:
            raise ValueError('There must be exactly 8 symbols on the board')
        self.flippedCards = takeRandomSymbols(symbols)#guardan las respuestas
        self.knownCards = list('?'*16)#se crea una lista con simbolos ?

    #representacion en cadena del tablero
    def __str__(self):
        return stringifyBoardList(self.knownCards)

    #muestra las cartas seleccionadas y regresa true si son pareja
    def show(self, card1, card2):
        if card1 not in positions or card2 not in positions:
            raise ValueError('Select only the cards on the board')
        if card1 == card2:#no se puede seleccionar la misma carta dos veces
            raise ValueError('Can\'t select the same card')
        index1, index2 = positions.index(card1), positions.index(card2)
        to_show = self.knownCards[:]
        to_show[index1] = self.flippedCards[index1]#se voltan las cartas para poder verlas
        to_show[index2] = self.flippedCards[index2]
        print stringifyBoardList(to_show)#se muestran las cartas
        if to_show[index1] == to_show[index2]:#si las cartas tienen el mismo simbolo
            self.knownCards = to_show#se actuliza la lista de las cartas que ya tienen par
            return True
        return False#si no son los mismos simbolos
