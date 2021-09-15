print("Введите натуральное число: ")
num = int(input())
last = int(str(num)[len(str(num))-1])

if last % 2 == 0:
    print("Число оканчивается четной цифрой")
else:
    print("Число оканчивается нечетной цифрой")