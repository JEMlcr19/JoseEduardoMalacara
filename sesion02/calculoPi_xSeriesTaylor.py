import math
acumulador = 0.0
division_acual = 1.0
contador = 0

while division_acual > 0.0052:
    contador += 1
    division_acual = 1/contador

    if contador % 2 != 0:
        if essuma:
            acumulador += division_acual
        else:
            acumulador -= division_acual
        essuma = not essuma

print("El cuarto del area es: ",acumulador)
pi = acumulador * 4
print("Pi es igual a: ", pi)

