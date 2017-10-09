# -*- coding: utf-8 -*-
import shelve

class Player:
    def __init__(self, name, passw):
        self.name = name
        self.password = passw
        self.games = 0
        self.wins = 0
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

    #representacion en casdena del jugador
    def __str__(self):
        rep = "\n  +-----------"
        rep += "\n  |   Jugador: " + self.name
        rep += "\n  |      ganadas        ->  " + str(self.wins)
        rep += "\n  |      perdidas       ->  " + str(self.games - self.wins)
        rep += "\n  |      total jugados  ->  " + str(self.games)
        rep += "\n  +-----------"
        return rep

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
