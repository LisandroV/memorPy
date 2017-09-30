# -*- coding: utf-8 -*-
from clases.player import Player

#funcion para registrar un nuevo jugador
def signUp():
    print "\nHora de crear tu usuario!!"

    #obtener nombre del jugador
    while True:
        opt = raw_input("Nombre de usuario: ")
        if len(opt) < 3:
            print "\nNombre demasiado corto :S, debe al menos 3 caracteres"
        elif not Player.valid_unique_name(opt):
            print "\nEl jugador '" + opt + "' ya existe, elije otro nombre."
        else:
            break
    name = opt

    while True:
        #obtener contraseña
        print "Contraseña: "
        while True:
            opt = raw_input()
            if Player.valid_passw_len(opt):
                break
            print "La contraseña debe contener 5 caracteres o más, intenta con otra"
        passwd = opt

        #confirmacion de contraseña
        print "Confirma tu contraseña:"
        opt = raw_input()
        if opt == passwd:
            break
        print "Las contraseñas no coinciden, escoje otra contraseña"

    return Player(name,passwd)
