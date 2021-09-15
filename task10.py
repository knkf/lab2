print("Введите натуральное число: ")
num = int(input())
if num % 2 == 0:
    print("Число является четным")
else:
    print("Число не является четным")
strNum = str(num)
if strNum[len(strNum)-1] == "7":
    print("Число оканчивается на 7")
else:
    print("Число не оканчивается на 7")
