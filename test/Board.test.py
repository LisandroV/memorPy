import sys
sys.path.append('../api/clases')
from board import Board

#board = Board(range(8))
#print board
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
print board
