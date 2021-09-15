#task7
import math
print("Введите значение Х: ")
x = int(input())
if x > 0:
    y = math.sin(x)*math.sin(x)
else:
    y = 1 - 2*math.sin(x*x)
print(y)