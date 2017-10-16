opts = "abcdef"

#la funcion valida la entrada delusuario
#recibe la opcion selecionada y el numero de opciones que hay
def valid_option(options):
    while True:
        opt = raw_input()
        if opt in list(opts[:options]):
            return opt
        print "la opcion '" + opt + "' no es valida, intenta de nuevo."
