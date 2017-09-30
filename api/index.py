# -*- coding: utf-8 -*-
from services.input_validation import *
from menu_functions.signup import *
from menu_functions.signin import *
from clases.player import Player

print "Hola, esto es memorPy, un juego de memorama =D"
print "  a) Registrar usuario"
print "  b) Iniciar sesión"
while True:
    opt = raw_input()
    if valid_input(opt, 2):
        break
    print "la opcion '" + opt + "' no es valida, intenta de nuevo."
if opt == 'a':
    player = signUp()
else:
    player = signIn()
