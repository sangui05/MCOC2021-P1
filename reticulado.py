import numpy as np
from scipy.linalg import solve
from barra import Barra
import numpy as np
from scipy.linalg import solve
from barra import Barra
#bar = Barra()
class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        
        


    def agregar_nodo(self, x, y, z=0):
        
        

        print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos

        self.xyz[numero_de_nodo_actual,:] = [x, y, z]

        self.Nnodos += 1
        
        return 0

    def agregar_barra(self, barra):
        
        self.barras.append(barra)        
        
        return 0

    def obtener_coordenada_nodal(self, n):
        
        corn = self.xyz[n,:]
        
        
        print(f"la posicion del nodo {n} es en las cordenadas =  {corn}")
        return corn
    def calcular_peso_total(self):
        pesototalbarras = 0
        for barra in self.barras:
            w_barra= barra.calcular_peso()
            pesototalbarras+= w_barra
        
        return pesototalbarras

    def obtener_nodos(self):
        
        return self.xyz

    def obtener_barras(self):
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        
        """Implementar"""	
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        """Implementar"""	
        
        return 0


    def ensamblar_sistema(self):
        
        """Implementar"""	
        
        return 0



    def resolver_sistema(self):
        
        """Implementar"""	
        
        return 0

    def obtener_desplazamiento_nodal(self, n):
        
        """Implementar"""	
        
        return 0


    def obtener_fuerzas(self):
        
        """Implementar"""	
        
        return 0


    def obtener_factores_de_utilizacion(self, f):
        
        """Implementar"""	
        
        return 0

    def rediseñar(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0







    def __str__(self):

        s = "Soy un reticulado :) \n"

        s += "Nodos: \n"

        for i in range(self.Nnodos):
            s += f"{i} : ({self.xyz[i][0]}, {self.xyz[i][1]}, {self.xyz[i][2]})\n"
            i += 1

        s += "Barras: \n"

        h = 0
        for i in self.barras:
            s += f"{h} : [{self.barras[h].ni} {self.barras[h].nj}]\n"
            h += 1

        return s

