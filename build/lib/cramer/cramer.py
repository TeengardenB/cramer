
#   _____ _____            __  __ ______ _____      _____       
#  / ____|  __ \     /\   |  \/  |  ____|  __ \    |  __ \      
# | |    | |__) |   /  \  | \  / | |__  | |__) |   | |__) |   _ 
# | |    |  _  /   / /\ \ | |\/| |  __| |  _  /    |  ___/ | | |
# | |____| | \ \  / ____ \| |  | | |____| | \ \   _| |   | |_| |
#  \_____|_|  \_\/_/    \_\_|  |_|______|_|  \_\ (_)_|    \__, |
#                                                          __/ |
#                                                         |___/
# Esta es una librería diseñada para resolver sistemas de ecuaciones lineales mediante el método de resolución
# de cramer.
# Para poder funcionar correctamente, es necesario contar con un sistema con misma cantidad de incógnitas que ecuaciones

import numpy as np

class cramer:

    def __init__(self , a):
        self.dim = np.shape(a)[0] 
        self.resul = np.copy(a[:,self.dim])
        self.a = a

        #Creacion de la primera matriz
        self.md = np.copy(a[:,range(0,self.dim)])
        p2 = self.md[range(0,2),:]
        self.md = np.vstack([self.md , p2])

    def matr(self):
        #esta funcion crea una array de arrays con las matrices con las que se arman todos los deltas.
        #para hacerlo, primero crea una lista y le agrega al principio la primera matriz, que queda excenta del bucle

        mat = []
        mat.append(self.md)

        for i in range(0 , self.dim):
            m = np.copy(self.a[:,range(0,self.dim)])
            m[:,i] = self.resul
            p2 = m[range(0,2),:]
            m = np.vstack([m , p2])
            mat.append(m)
        
        mat = np.asarray(mat)
        return mat

    def delta(self , arr):
        #esta función se encarga de generar deltas cuando recibe funciones como entrada
        #devuelve al final un único valor, correspondiente al delta obtenido

        posi = []
        for scroll in range(0, self.dim):
            y = scroll
            fila = []
            for x in range(0 , self.dim):
                fila.append(arr[y , x])
                y += 1
            posi.append(fila)

        posi = np.asarray(posi)


        nega = []
        for scroll in range(0, self.dim):
            y = scroll
            fila = []
            for x in range(self.dim - 1  , -1 , -1):
                fila.append(arr[y , x])
                y += 1
            nega.append(fila)

        nega = np.asarray(nega)

        

        pos = 0
        for i in range(0 , np.shape(posi)[0]):
            pos += np.multiply.reduce(posi[i])

        neg = 0
        for i in range(0 , np.shape(nega)[0]):
            neg += np.multiply.reduce(nega[i])

        delta = (pos - neg)
        return delta



