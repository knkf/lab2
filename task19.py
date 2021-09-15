print("Введите трёхзначное число: ")
num = int(input())

mun = str(num)[2]
mun += str(num)[1]
mun += str(num)[0]
print(int(mun))
