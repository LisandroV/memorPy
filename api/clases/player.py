# -*- coding: utf-8 -*-
import shelve

class Player:
    def __init__(self, name, passw):
        self.name = name
        self.password = passw
        self.games = 0
        self.wins = 0
        self.lives = 3
        if len(self.name) < 3:
            raise ValueError('Nombre de jugador demasiado corto')
        #validacion para unicidad de jugadores
        if not Player.valid_unique_name(self.name):
            raise ValueError('Ya existe ese nombre de jugador')
        #validacion para longitud de contraseña
        if not Player.valid_passw_len(self.password):
            raise ValueError('La contraseña debe contener 5 caracteres mínimo')
        #se guarda el usuario en la base de datos
        players_db = shelve.open("./Players_DB.dat")
        players_db[self.name]=self
        players_db.close()

    #se reinician los valores de las partidas jugadas
    def clear_history(self):
        self.games = 0
        self.wins = 0
        players_db = shelve.open("./Players_DB.dat")
        players_db[self.name] = self
        players_db.close()

    #sube el numero de juegos y partidas ganadas
    def has_won(self, won):
        if won:
            self.wins = self.wins + 1
        self.games = self.games + 1
        players_db = shelve.open("./Players_DB.dat")
        players_db[self.name] = self
        players_db.close()


    def reset_lives(self):
        self.lives = 3

    def alive(self):
        return self.lives > 0
    #representacion en casdena del jugador
    def __str__(self):
        rep = "\n  +-----------"
        rep += "\n  |   Jugador: " + self.name
        rep += "\n  |      ganadas        ->  " + str(self.wins)
        rep += "\n  |      perdidas       ->  " + str(self.games - self.wins)
        rep += "\n  |      total jugados  ->  " + str(self.games)
        rep += "\n  +-----------"
        return rep

    def print_lives(self):
        hearts = ""
        for i in range(self.lives):
            hearts += u"\u2665" + "  "
        for i in range(3 - self.lives):
            hearts += u"\u2661" + "  "
        print self.name + "  " + hearts

    #metodo que resta una vida al jugador
    def lost(self):
        self.lives = self.lives - 1

    #metodo estático para validar uncicidad de los jugadores
    @staticmethod
    def valid_unique_name(name):
        players_db = shelve.open("./Players_DB.dat")
        unique = name in players_db
        players_db.close()
        return not unique

    #metodo estatico para la validacion de longitud de contraseña
    @staticmethod
    def valid_passw_len(passw):
        return len(passw) > 4

    #metodo que encuentra al usiario con ese nombre y esa contaseña
    #sirve para hacer log in
    @staticmethod
    def findPlayer(name, passwd):
        players_db = shelve.open("./Players_DB.dat")
        try:
            foundPlayer = players_db[name]
            players_db.close()
            #si el jugador existe y tiene la misma contraseña
            if foundPlayer.password == passwd:
                return foundPlayer
        except:
            pass
        return None
