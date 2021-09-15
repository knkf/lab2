print("Введите натуральное число: ")
num = int(input())

a = int(str(num)[0])
b = int(str(num)[2])

if a == b:
    print("Число является палиндромом")
