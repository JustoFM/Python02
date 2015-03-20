# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# Sistemas Distribuidos
# Seminario 2 con fecha 20/03/2015

# Autores:
#   Justo Manuel Fuentes Meléndez
#   Christian Suárez Picón

# Explicación del Programa:
# Este programa se encarga de obtener la lista más larga de palabras encadenadas, es decir,
# una lista con una sucesión de palabras en la que la palabra i+1 empieza por la letra por la que
# acaba la palabra i.

#Funcion que genera la lista más larga
def creaListaMasLarga(fichero):
    ListaPokemon = open(fichero, 'r').read().split() #Leemos el fichero y cargamos los pokemon en una lista
    
    ListaAuxiliar = [] #Lista en la que almacenamos las cadenas que vamos formando
    ListaMasLarga = [] #Lista en la que almacenamos la lista mas larga hasta el momento
    
    for pokemon in ListaPokemon: #Recorremos la ListaPokemon
        ListaAuxiliar.append(pokemon) #Añadimos el pokemon a la ListaAuxiliar
        i = 0
        while i < len(ListaPokemon): #Recorremos la ListaPokemon en busca del siguiente pokemon de la lista
            if(ListaPokemon[i] not in ListaAuxiliar and ListaAuxiliar[-1][-1] == ListaPokemon[i][0]):
                #Si no está en la ListaAuxiliar y acaba con la misma letra con la que acaba el pokemon recien añadido.
                ListaAuxiliar.append(ListaPokemon[i]) #Añadimos el pokemon a ListaAuxiliar
                i = 0 #Reiniciamos el bucle para volver a buscar otro pokemon
            else: #En otro caso
                i += 1 #Vemos si el siguiente pokemon coincide
        if (len(ListaAuxiliar)>len(ListaMasLarga)): # Vemos si la ListaAuxiliar es mas larga que ListaMasLarga
    		del ListaMasLarga[:] # Borramos ListaMasLarga
    		ListaMasLarga.extend(ListaAuxiliar) # Amplimos ListaMasLarga con ListaAuxiliar
        del ListaAuxiliar[:] # Borramos ListaAuxliar
    print ListaMasLarga # Pintamos el contenido de ListaMasLarga

#Función main. Pide el nombre del fichero donde se encuentran los nombres(pokemons en este caso).
fichero = raw_input("Introduzca el nombre del fichero: ")
print "Lista más larga encontrada: "
creaListaMasLarga(fichero)

# <codecell>