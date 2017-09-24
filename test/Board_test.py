import unittest
import pytest
import sys
sys.path.append('api/clases')
from board import Board

board = Board([
u"\U0001F436",
u"\U0001F525",
u"\u262D",
u"\U0001F335",
u"\U0001F4BB",
u"\U0001F4BE",
u"\U0001F4A9",
u"\U0001F428",
])

class BoardTest(unittest.TestCase):
    #esta prueba solo imprime el tablero
    def test__str__method(self):
        print "\n----------------SHOULD PRINT THE MEMORAMA BOARD---------------------"
        print board
