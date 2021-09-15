# task6
import datetime
now = datetime.datetime.now()
print("Введите год рождения: ")
yearOfBirth = int(input())
print("Введите номер месяца рождения: ")
monthOfBirth = int(input())
age = now.year - yearOfBirth - 1
if monthOfBirth == now.month:
    age+=1
print("Возраст: ", age)
