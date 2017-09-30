opts = "abcdef"

#la funcion valida la entrada delusuario
#recibe la opcion selecionada y el numero de opciones que hay
def valid_input(inpt, options):
    return inpt in list(opts[:options])
