# -*- coding: utf-8 -*-
from clases.player import Player

#funcion para que el usuario inicie sesión
def signIn():
    print "\n\nIngresando ..."
    while True:
        name = raw_input(" ---- Nombre: ")
        passwd = raw_input(" ---- Contraseña: ")
        foundPlayer = Player.findPlayer(name, passwd)
        if foundPlayer:
            return foundPlayer
        print "\nContraseña o nombre de usuario incorrectos. Sorry, ingresa de nuevo"
