import numpy as np
from constantes import g_, ρ_acero, E_acero


class Barra(object):

	"""Constructor para una barra"""
	def __init__(self, ni, nj, seccion):
		super(Barra, self).__init__()
		self.ni = ni
		self.nj = nj
		self.seccion = seccion
		
	

	def obtener_conectividad(self):
		return [self.ni, self.nj]

	def calcular_area(self):
		A = seccion.area
		return A

	def calcular_largo(self, reticulado):
		"""Devuelve el largo de la barra.
		xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
		xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
		"""
		xi = reticulado.obtener_coordenada_nodal(self.ni)
		xj = reticulado.obtener_coordenada_nodal(self.nj)
		dij = xi-xj
		return np.sqrt(np.dot(dij,dij))

	def calcular_peso(self, reticulado):
		
		L = self.calcular_largo(reticulado)
		Peso = seccion.peso
		return Peso * L
'''

    def obtener_rigidez(self, ret):
        
        """Implementar"""	
        
        return 0

    def obtener_vector_de_cargas(self, ret):
        
        """Implementar"""	
        
        return 0


    def obtener_fuerza(self, ret):
        
        """Implementar"""	
        
        return 0




    def chequear_diseño(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0





    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


    def rediseñar(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0
'''

