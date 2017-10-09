# -*- coding: utf-8 -*-
import sys
sys.path.append('api/clases')
from player import Player
import unittest
import pytest
import os

#funcion que borra a base de datos para poder hacer pruebas
def del_db():
    try:
        os.remove("Players_DB.dat")
    except:
        pass

class PlayerTest(unittest.TestCase):

    #debe dejar crear el jugador
    def test__init__(self):
        del_db()
        pl1 = Player("n-droid", "Aws23RdfDffi")
        del_db()

    #no deja que se creen dos jugadores con el mismo nombre
    def test_not_create_invalid_name(self):
        del_db()
        pl1 = Player("n-droid", "Aws23RdfDffi")
        self.assertRaises(ValueError, Player, "n-droid", "____asfhbsd")
        del_db()

    #no debe crear un jugado con una contraseña de menos de 5 caracteres
    def test_not_create_invalid_password(self):
        self.assertRaises(ValueError, Player, "n-droid", "uno")
        del_db()

    def test_str_rep(self):
        print "\n----------------SHOULD PRINT THE PLAYER PROFILE---------------------"
        del_db()
        pl1 = Player("n-droid", "Aws23RdfDffi")
        print pl1
        del_db()
