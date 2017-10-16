# -*- coding: utf-8 -*-
from clases.player import Player
from clases.board import Board
from services.cards_option_validation import *
import time
import os

def play(player):
    #simbolos con los que va a trabajar el memorama
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
    board = Board(symbols)
    player.reset_lives()
    print "\n\n   ~ ~ C O M E N Z A M O S ~ ~  \n"
    board.show_flippedBoard()
    print "\n  ¡¡Recuerda todos los que puedas!!!"
    time.sleep(7)
    os.system("reset")

    while player.alive() and not board.has_won():
        print board
        player.print_lives()
        while True:
            try:
                cards = raw_input("escoge tus cartas: ")
                valid_op_card(cards)#se valida que la entrada este bien
                was_right = board.show(cards[0], cards[1])
                break
            except Exception as e:
                print e
        if was_right:
            print "¡¡PERFECTO!!"
        else:
            print "¡Muuuuuuy Mal!"
            player.lost()
        time.sleep(5)
        os.system("reset")

    print board
    if player.alive() and board.has_won():
        print "\n      ¡¡¡¡FECLICIDADES  YA GANASTE!!!!\n\n"
        player.has_won(True)
    else:
        print "\n    Ya perdiste, ni modo :s\n\n"
        player.has_won(False)
    print player
