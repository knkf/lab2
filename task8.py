#task8
import math
print("Введите значение Х: ")
x = int(input())
if x > 0:
    y = math.sin(x*x)
else:
    y = 1 + 2*math.sin(x)*math.sin(x)
print(y)
