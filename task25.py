print("Введите натуральное число: ")
num = int(input())
print("Число десятков: ", str(num//10)[len(str(num // 10))-1])
print("Число единиц: ", num % 10)
