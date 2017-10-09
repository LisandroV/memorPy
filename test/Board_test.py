# -*- coding: utf-8 -*-
import sys
sys.path.append('api/clases')
from board import Board
import unittest
import pytest
from random import choice
from random import randint

symbols = [
    u"\U0001F436",
    u"\U0001F525",
    u"\u262D",
    u"\U0001F335",
    u"\U0001F4BB",
    u"\U0001F4BE",
    u"\U0001F4A9",
    u"\U0001F428",
]

class BoardTest(unittest.TestCase):
    #esta prueba solo imprime el tablero
    def test__str__method(self):
        print "\n----------------SHOULD PRINT THE MEMORAMA BOARD---------------------"
        board = Board(symbols)
        print board

    def test_init_error(self):
        #si la longitud de la lista de simbolos es diferente de 8 no se podra crear el tablero
        self.assertRaises(ValueError, Board, range(6))#se intenta crear tablero con 6 elementos

    def test_show_method(self):
        print "\n----------------SHOULD SHOW THE SAME CARD---------------------"
        positions = list('abcdefghijklmnop')
        board = Board(symbols)
        sym = choice(symbols)
        same_sym = [i for i, x in enumerate(board.flippedCards) if x == sym]#indices de los simbolos que son iguales a
        same_a = positions[same_sym[0]]
        same_b = positions[same_sym[1]]
        self.assertTrue( board.show(same_a, same_b) )

    def test_show_method_assert_false(self):
        print "\n----------------SHOULD NOT SHOW THE SAME CARD---------------------"
        positions = list('abcdefghijklmnop')
        board = Board(symbols)
        sym = choice(symbols)
        rnd = randint(0, 6)#se selecciona un simbolo al azar
        diff_a = positions[board.flippedCards.index(symbols[rnd])]
        diff_b = positions[board.flippedCards.index(symbols[rnd + 1])]#las cartas seleccionadas son diferentes
        self.assertFalse( board.show(diff_a, diff_b) )

    def test_should_raise_same_card(self):
        #si se escoje la misma carta debe lanzar un error
        positions = list('abcdefghijklmnop')
        card_selected = choice(positions)
        board = Board(symbols)
        self.assertRaises(ValueError, board.show, card_selected, card_selected)
