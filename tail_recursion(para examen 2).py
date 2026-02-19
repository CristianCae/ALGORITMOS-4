def suma_lista_normal(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + suma_lista_normal(lista[1:])



# Conversion a tail
def suma_lista_tail(lista, acumulador=0):
    if len(lista) == 0:
        return acumulador
    return suma_lista_tail(lista[1:], acumulador + lista[0])

print(suma_lista_tail(30))

# --------------------------------------------------------------------------
def potencia_normal(base, exp):
    if exp == 0:
        return 1
    return base * potencia_normal(base, exp -1)

# conversion a tail
def potencian_tail(base, exp, acumulador=1):
    if exp == 0:
        return acumulador
    return potencian_tail(base, exp -1, acumulador * base)
    
#-----------------------------------------------------------------------------
def invertir_tail(lista, acumulador=None):
    if acumulador is None:
        acumulador = [] # Retorna una lista vacia

    if len(lista) == 0:
        return acumulador # Ayuda a guardar la lista invertida

    return invertir_tail(lista[1:], [lista[0]] + acumulador)
