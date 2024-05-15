class FiguraGeometrica():

    ubicacion_x = 0
    ubicacion_y = 0

    def _init_(self):
        None
    def get_area(self):
        return 9999999.9
    
    #def modificar_x(self.x):
        self.ubicacion_x = x
    #def modificar_y(self.y):
        self.ubicacion_y = y
    
class Rectangulo(FiguraGeometrica):
    alto = 0.0
    base = 0.0

    def _init_(self,alto,base):
        self.alto = float(alto)
        self.base = float(base)

    def _str_(self):
        return "Es un rectangulo, con area: " + str(self.get_area())

    def get_area(self):
      return self.alto * self.base
    
class Circulo(FiguraGeometrica):
    None
class Triangulo(FiguraGeometrica):
    None

import turtle

prueba = Rectangulo(2,2)
print(str(prueba.get_area()))
        

    

        