# -*- coding: utf-8 -*-
from services.input_validation import *
from menu_functions.signup import *
from menu_functions.signin import *
from menu_functions.play import *
from clases.player import Player

print "Hola, esto es memorPy, un juego de memorama =D"
print "  a) Registrar usuario"
print "  b) Iniciar sesión"
opt = valid_option(2)
player = signUp() if opt == 'a' else signIn()
print "\n\nHola " + player.name + "!  ¿que quieres hacer?"
print "  a) Jugar"
print "  b) Ver tu historial"
print "  c) Borrar historial"
opt = valid_option(3)
if opt == 'a':
    play(player)
