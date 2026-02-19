def potencia(a, b):
    if b == 0:
        return 1
    return a * potencia(a, b -1) # Se ejecuta n veces



def potencia_optimizado(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        mitad = potencia_optimizado(a, b // 2)      # se evirta varios llamados recursivos a la hora de hacer la potencia
        return mitad * mitad
    else:
        return a * potencia_optimizado(a, b -1)
    

    ## recursivo, que se entregue un numero cualquiera y entregue la suma de ese numero


def suma_digitos(n):
    if n == 0:                     ## explicacion foto en el celular 19/02/ h: 07:45
        return 0
    digito = n % 10
    return digito + suma_digitos(n // 10)

#Busqueda Binaria

    def Busqueda_Binaria(Lista, objetivo, inicio=0, fin=None):
        if fin == None:
            fin = len(lista) - 1
        # caso base: rango invalido (Elemento no encontrado)
        if inicio > fin:
            return -1
        # calcular punto medio
        medio = (inicio + fin) // 2
        # comparar y decidir en que mitad buscar
        if lista[medio] == objetivo:
            return medio # Encontrado
        elif objetivo < lista[medio]:
            #Buscar en la mitad izquierda
            return Busqueda_Binaria(Lista. Objetivo, inicio, medio -1)
        else:
            # Buscar en la mitad de la derecha
            return Busqueda_binaria(lista, objetivo, medio +1, fin)
        
# Lista de todas las permutaciones posibles

    def permutaciones(lista):
        if len(lista) <=1:
            return[lista[:]] # Retornasr copia de la lista
        
        resultado = []

        # Para cada elemento de la lista
        for i in range(len(lista)):
            #elemento actual
            elemento = lista[1]
            #lista sin el elemento actual
            resto = lista[:1] + lista[i+1:]
            #obtener permutaciones del resto
            for pem in permutaciones(resto):
                #Agregar elemento al inicio de cada permutacion
                resultado.append([elemento] + perm)
        
        return resultado
    


        