print("Введите натуральное число: ")
num = int(input())
a = int(str(num)[0])
b = int(str(num)[1])
c = int(str(num)[2])
print(a == b == c)
print(a == b or b == c or a == c)

