opts = "abcdefghijklmnop"

#valida que la opcion de cartas elegidas sea valida
def valid_op_card(option):
    if len(option) != 2:
        raise Exception("\nDebes escoger las cartas de la forma: 'ap'")
