print("Введите натуральное число: ")
num = int(input())

a = int(str(num)[0])
b = int(str(num)[1])

if a > b:
    print("Первая цифра больше второй")
if a < b:
    print("Вторая цифра больше первой")
else:
    print("Цифры одинаковы")

if a == b:
    print("Цифры числа одинаковы")
else:
    print("Цифры числа не одинаковы")
