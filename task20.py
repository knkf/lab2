print("Введите трёхзначное число: ")
num = input()
a = num[1]
a += num[2]
a += num[0]
print(a)