from numpy import pi, sqrt
from constantes import g_, ρ_acero
 
class Circular(object):
    """define una seccion Circular"""

    def __init__(self, D, Dint):
        super(Circular, self).__init__()
        self.D
        self.Dint

    def area(self):
        
        A = pi*(self.D**2 - self.Dint**2)/4	
        
        return A

    def peso(self):

        
        peso = g_*ρ_acero*self.area()
        
        return peso

    def inercia_xx(self):

        
        Ixx = pi * (self.D**2 - self.Dint**2)/4
        
        return Ixx

    def inercia_yy(self):

        return self.inercia_xx

