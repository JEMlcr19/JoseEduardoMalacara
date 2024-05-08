import random
import math

cuantos = 1000
cuantossi = 0
for i in range(cuantos):
    x = random.random()
    y = random.random()

    y_calculada = math.sqrt(1-x*x)
    if y > y_calculada:
        None
    else:
        cuantossi += 1

cuarto_area = float(cuantossi)/float(cuantos)
print(cuarto_area)
print("Pi es igual a: ",cuarto_area*4)