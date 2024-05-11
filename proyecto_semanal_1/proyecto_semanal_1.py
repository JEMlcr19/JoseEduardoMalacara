import math

def area_rectangulo():
    print("Calculemos el area de un rectangulo")
    lado_a = float(input("Cuanto mide el lado A del Rectangulo: "))
    lado_b = float(input("Cuanto mide el lado B del Rectangulo: "))

    rectangulo = lado_a * lado_b

    print("El area del rectangulo es: ",rectangulo,"cm2")



def area_triangulo():
    print("Calculemos el area de un triángulo")
    lado_a = float(input("Cuanto mide el lado A del Triángulo: "))
    lado_b = float(input("Cuanto mide el lado B del Triángulo: "))
    lado_c = float(input("Cuanto mide el lado C del Triángulo: "))

    p_t = (lado_a + lado_b + lado_c)/2
    triangulo = (math.sqrt(p_t * (p_t - lado_a) * (p_t - lado_b) * (p_t - lado_c)))
    print("El area del Triángulo es: ",triangulo,"cm2")


def area_circulo():
    print("Calculemos el area de un circulo")
    diametro = float(input("Cuanto mide el diametro del circulo: "))
    radio = diametro / 2
    circulo = math.pi * (radio * radio)
    print("El area del circulo es: ",circulo,"cm2")


print("Selecciona el area de la figura que deseas calcular el area")
print("1 - Rectangulo")
print("2 - Triangulo")
print("3 - Circulo")

opcion = input("Opción: ")

if opcion == "1":
    area_rectangulo()
elif opcion == "2":
    area_triangulo()
elif opcion == "3":
    area_circulo()
else:
    print("Opción invalida. Por favor elije una opcion disponible.")
