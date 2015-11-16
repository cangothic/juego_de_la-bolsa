__author__ = 'rocka'
def es_un_numero(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

def es_entero(numero):
    if(numero-int(numero)!=0):
        return False
    else:
        return True