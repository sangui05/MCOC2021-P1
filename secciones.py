from numpy import pi, sqrt, nan
from numpy.random import rand
from constantes import g_, ρ_acero, mm_
 
class Circular(object):
    """define una seccion Circular"""

    def __init__(self, D, Dint, color=rand(3)):
        super(Circular, self).__init__()
        self.D = D
        self.Dint = Dint
        self.color = color  #color para la seccion

    def area(self):
        return pi*(self.D**2 - self.Dint**2)/4

    def peso(self):
        return self.area()*ρ_acero*g_

    def inercia_xx(self):
        return pi*(self.D**4 - self.Dint**4)/4

    def inercia_yy(self):
        return self.inercia_xx()

    def nombre(self):
        return f"O{self.D*1e3:.0f}x{self.Dint*1e3:.0f}"

    def __str__(self):
        return f"Seccion Circular {self.nombre()}"


        
#Mas adelante, no es para P1E1

class SeccionICHA(object):
    """Lee la tabla ICHA y genera una seccion apropiada"""

    def __init__(self, denominacion, base_datos="Perfiles ICHA.xlsx", debug=False, color=rand(3)):
        super(SeccionICHA, self).__init__()
        self.denominacion = denominacion
        self.color = color  #color para la seccion
        palabras = []
        palabra = ''
        for i in self.denominacion:
            if i == 'H':
                j = self.denominacion.index(i) +1
                if self.denominacion[j] == 'R':
                    self.base_datos = pd.read_excel(base_datos,sheet_name='HR', header=None)
                else:
                    self.base_datos = pd.read_excel(base_datos, sheet_name='H', header=None)
                continue

            if i == 'x':
                palabras.append(float(palabra))
                palabra = ''

            else:
                palabra += i

        palabras.append(float(palabra))



        for i in range(0, len(self.base_datos[1])):
            if self.base_datos[1][i] == palabras[0]:
                if self.base_datos[3][i] == palabras[1]:
                    if self.base_datos[5][i] == palabras[2]:
                        self.posicion = i


    def area(self):

        area = self.base_datos[9][self.posicion]

        return area

    def peso(self):

        peso = self.base_datos[3][self.posicion]

        return 0

    def inercia_xx(self):

        inercia_xx = self.base_datos[10][self.posicion]
        return inercia_xx

    def inercia_yy(self):

        inercia_yy = self.base_datos[14][self.posicion]
        return inercia_yy

    def __str__(self):
        return f"Seccion ICHA {self.denominacion}, area {self.area()}"
