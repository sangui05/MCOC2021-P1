
from scipy.linalg import solve
from barra import Barra
import numpy as np
from scipy.linalg import solve
from secciones import SeccionICHA
from barra import Barra
from matplotlib.pylab import *
import h5py as h5
#bar = Barra()
class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 1

    def __init__(self):
        super(Reticulado, self).__init__()

        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        self.Ndimensiones = 3
        self.has_solution = False




    def agregar_nodo(self, x, y, z=0):


        #FUNCION AGREGAR NODO FUNCIONAL Y SIN PROBLEMAS
        """
            print(f"Quiero agregar un nodo en ({x} {y} {z})")
            numero_de_nodo_actual = self.Nnodos
    
            self.xyz[numero_de_nodo_actual,:] = [x, y, z]
    
            self.Nnodos += 1
    
            return 0"""
        if self.Nnodos+1 > Reticulado.__NNodosInit__:
            self.xyz.resize((self.Nnodos+1,3))
        self.xyz[self.Nnodos,:] = [x, y, z]
        self.Nnodos += 1
        if z != 0.:
            self.Ndimensiones = 3

    def agregar_barra(self, barra):

        self.barras.append(barra)

        return 0

    
        if n >= self.Nnodos:
            return 
        return self.xyz[n, :]
    def calcular_peso_total(self):
        pesototalbarras = 0
        for barra in self.barras:
            w_barra= barra.calcular_peso(self)
            pesototalbarras+= w_barra

        return pesototalbarras

    def obtener_nodos(self):

        #return self.xyz FUNCINAL Y SIN PROBLEMAS QUITAR # SI SE DESEA VERIFICAR FUNCIONALIDAD
        return self.xyz[0:self.Nnodos,:].copy()

    def obtener_barras(self):

        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        print(f"Agregando una restriccion en: ({nodo} {gdl} {valor})")

        if nodo not in self.restricciones:  #Si el nodo no está en las restricciones, se agrega

            self.restricciones[nodo] = [[gdl, valor]]
            
        else :
            self.restricciones[nodo].append([gdl, valor])
            

        #print (restricciones)


    def agregar_fuerza(self, nodo, gdl, valor):

        print(f"Agregando una fuerza en: ({nodo} {gdl} {valor})")

        if nodo not in self.cargas: #Si no existe el nodo, se agrega.

            self.cargas[nodo] = [[gdl, valor]]
            
        else:

            self.cargas[nodo].append([gdl, valor])
            return 0

        #print (cargas)

    #Actualizacion de fn agregar_restriccion/fuerza funcionando    


    #emsamblar sistema parcialmente realizado
    def ensamblar_sistema(self, factor_peso_propio=0):
        factor_peso_propio=0


        Nm = self.Nnodos*3 #según las dimensiones
        self.K = np.zeros((Nm,Nm),dtype=np.double)
        self.f = np.zeros((Nm),dtype=np.double)
        self.u = np.zeros((Nm),dtype=np.double)

        for i,b in (self.barras):

            ke = b.obtener_rigidez(self)
            fe = b.obtener_vector_de_cargas(self,factor_peso_propio)
            
            ni,nj = b.obtener_conectividad()

        #MDR
            if self.Ndimensiones == 2:
                d = [2*ni, 2*ni+1 , 2*nj, 2*nj+1]
            else:
                d = [3*ni, 3*ni+1, 3*ni+2 , 3*nj, 3*nj+1, 3*nj+2]

            for i in range(self.Ndimensiones*2):
                p = d[i]
                for j in range(self.Ndimensiones*2):
                    q = d[j]
                    self.K[p,q] += ke[i,j]
                self.f[p] += fe[i]


        for nodo in self.cargas:
            for carga in self.cargas[nodo]:
                gdl = carga[0]
                valor = carga[1]

                self.gdl_global = self.Ndimensiones*nodo + gdl
                self.f[self.gdl_global] = factor_cargas*valor



    # -----------------------------EJEMPLO CLASE PROFE--------------------------



    #       for e in self.barras: #recore las barras #barras tiene [N°barra | ni | nj]
    #           ni = self.barras[1]
    #           nj = self.barras[2]
    #
    #           ke = e.obtener_rigidez()
    #           fe = e.obtener_vector_de_carga()
    #           d = [3*ni,3*ni+1, 3*ni+2,3*nj,3*nj+1,3*nj+2]
    #
#3           for i in range(6):
    #               p = d[i]
    #               for j in range(6):
    #                   q = d[j]
    #                   K[p,q] += k_e[i,j]
    #               f[p] += f_e[i]
    #
    #           #agregar cargas puntuales
    #
    #3           for nodo in cargas:
        #                   print(nodo)
        #                   Ncargas = len(cargas[nodo])
        #                   print(Ncargas)
        #
        #                   for carga in range :
        #
        #                       gdl = cargas[nodo][0]
        #                       f = cargas[nodo][1]
        #                      print(f"Agregando carga de {f} en GDL {gdl}")
        #
        #                      gdl_global = 3*node + gdl
        #                      F[gdl_global] += f
        #
        #
        #

        #self.K #matriz rigidez
        #self.u # grados de libertad

        #---------------------FIN EJEMPLO PROFE----------------------------------------


    def resolver_sistema(self):

        # 0 : Aplicar restricciones
        Ngdl = self.Nnodos * self.Ndimensiones
        self.gdl_libres = np.arange(Ngdl)
        self.gdl_restringidos = []

        #Pre-llenar el vector u

        for nodo in self.restricciones:
            for restriccion in self.restricciones[nodo]:
                gdl = restriccion[0]
                valor = restriccion[1]

                self.gdl_global = self.Ndimensiones*nodo + gdl
                self.u[self.gdl_global] = valor

                self.gdl_restringidos.append(self.gdl_global)

        # con self.gdl_restringidos encuentro  self.gdl_libres
        self.gdl_restringidos = np.array(self.gdl_restringidos)
        self.gdl_libres = np.setdiff1d(self.gdl_libres, self.gdl_restringidos)


        #1 Particionar:


        self.Kff = self.K[np.ix_(self.gdl_libres, self.gdl_libres)]
        Kfc = self.K[np.ix_(self.gdl_libres, self.gdl_restringidos)]
        Kcf = Kfc.T
        Kcc = self.K[np.ix_(self.gdl_restringidos, self.gdl_restringidos)]
 
        uf = self.u[self.gdl_libres]
        uc = self.u[self.gdl_restringidos]

        ff = self.f[self.gdl_libres]
        fc = self.f[self.gdl_restringidos]

        # Solucionar Kff uf = ff
        uf = solve(self.Kff, ff - Kfc @ uc)

        self.u[self.gdl_libres] = uf

        self.has_solution = True

    def obtener_desplazamiento_nodal(self, n):
        if self.Ndimensiones == 2:
            dofs = [2*n, 2*n+1]
        elif self.Ndimensiones == 3:
            dofs = [3*n, 3*n+1, 3*n+2]
        else:
            print(f"Error en numero de dimensiones. Ndimensiones = {self.Ndimensiones == 2} ")

        return self.u[dofs]


    def obtener_fuerzas(self):
        
        fuerzas = np.zeros((len(self.barras)), dtype=np.double)
        for i,b in enumerate(self.barras):
            fuerzas[i] = b.obtener_fuerza(self)

        return fuerzas


    def obtener_factores_de_utilizacion(self, f, ϕ=0.9):
        
        FU = np.zeros((len(self.barras)), dtype=np.double)
        for i,b in enumerate(self.barras):
            FU[i] = b.obtener_factor_utilizacion(f[i], ϕ)

        return FU

    def rediseñar(self, Fu, ϕ=0.9):
        for i,b in enumerate(self.barras):
           print(f"\n\nBarra {i}")
           b.rediseñar(Fu[i], self, ϕ)



    def chequear_diseño(self, Fu, ϕ=0.9, silence=False):
        cumple = True
        for i,b in enumerate(self.barras):
            if not b.chequear_diseño(Fu[i], self, ϕ, silence=silence):
                if not silence:
                    print(f"----> Barra {i} no cumple algun criterio. ")
                cumple = False
        return cumple


    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        print(f"Agregando una restriccion en: ({nodo} {gdl} {valor})")

        if nodo in self.restricciones:  #Si el nodo no está en las restricciones, se agrega

            self.restricciones[nodo] = []
            self.restricciones[nodo].append([gdl, valor])
            return 0
        else :
            self.restricciones[nodo] = ([gdl, valor])
            return 0

        #print (restricciones)


        return 0

    def agregar_fuerza(self, nodo, gdl, valor):

        print(f"Agregando una fuerza en: ({nodo} {gdl} {valor})")

        if nodo in self.cargas: #Si no existe el nodo, se agrega.

            self.cargas[nodo] = []
            self.cargas.append([gdl, valor])
            return 0
        else:

            self.cargas[nodo] = ([gdl, valor])
            return 0

        #print (cargas)

    #Actualizacion de fn agregar_restriccion/fuerza funcionando    


    #emsamblar sistema parcialmente realizado
    def ensamblar_sistema(self, factor_peso_propio=0):
        factor_peso_propio=0


        Nm = self.Nnodos*3 #según las dimensiones
        self.K = np.zeros((Nm,Nm),dtype=np.float32)
        self.f = np.zeros(Nm)
        self.u = np.zeros(Nm)

        for e in (self.barras):

            ke = e.obtener_rigidez(self)
            fe = e.obtener_vector_de_cargas(self)
            wbarra = e.calcular_peso(self)
            ni,nj = e.obtener_conectividad(self)

            if factor_peso_propio == 0:
                factor_peso_propio [0, 0, 0]
                f = np.zeros(6)
            d = [3*ni,3*ni+1, 3*ni+2,3*nj,3*nj+1,3*nj+2]

            for i in range(6):
                p = d[i]
                for j in range(6):
                    q = d[j]
                    self.K[p,q] += ke[i,j]
                self.f[p] += fe[i]
            for n in range(self.Nnodos):
                for carga in self.cargas(n):
                    if len(carga)!= 0:
                        self.f[n*Nm+carga[0]] += carga[1]
            self.F.append(f)


            return 0




    # -----------------------------EJEMPLO CLASE PROFE--------------------------



    #       for e in self.barras: #recore las barras #barras tiene [N°barra | ni | nj]
    #           ni = self.barras[1]
    #           nj = self.barras[2]
    #
    #           ke = e.obtener_rigidez()
    #           fe = e.obtener_vector_de_carga()
    #           d = [3*ni,3*ni+1, 3*ni+2,3*nj,3*nj+1,3*nj+2]
    #
#3           for i in range(6):
    #               p = d[i]
    #               for j in range(6):
    #                   q = d[j]
    #                   K[p,q] += k_e[i,j]
    #               f[p] += f_e[i]
    #
    #           #agregar cargas puntuales
    #
    #3           for nodo in cargas:
        #                   print(nodo)
        #                   Ncargas = len(cargas[nodo])
        #                   print(Ncargas)
        #
        #                   for carga in range :
        #
        #                       gdl = cargas[nodo][0]
        #                       f = cargas[nodo][1]
        #                      print(f"Agregando carga de {f} en GDL {gdl}")
        #
        #                      gdl_global = 3*node + gdl
        #                      F[gdl_global] += f
        #
        #
        #

        #self.K #matriz rigidez
        #self.u # grados de libertad

        #---------------------FIN EJEMPLO PROFE----------------------------------------









        



    

 #       for e in self.barras: #recore las barras #barras tiene [N°barra | ni | nj]
 #           ni = self.barras[1] 
 #           nj = self.barras[2]
 #           
 #           ke = e.obtener_rigidez()
 #           fe = e.obtener_vector_de_carga()          
 #           d = [3*ni,3*ni+1, 3*ni+2,3*nj,3*nj+1,3*nj+2]
 #           
 #          for i in range(6):
 #               p = d[i]
 #               for j in range(6):
 #                   q = d[j]
 #                   K[p,q] += k_e[i,j]
 #               f[p] += f_e[i]
 #           
 #           #agregar cargas puntuales
 #           
 #         for nodo in cargas:
 #                   print(nodo)
 #                   Ncargas = len(cargas[nodo])
 #                   print(Ncargas)
 #                   
 #                   for carga in range :
 #                       
 #                       gdl = cargas[nodo][0]
 #                       f = cargas[nodo][1]
 #                      print(f"Agregando carga de {f} en GDL {gdl}")
 #                     
 #                      gdl_global = 3*node + gdl
 #                      F[gdl_global] += f
           # 
           #
           #
           
           #self.K #matriz rigidez
           #self.u # grados de libertad
