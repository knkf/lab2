print("Введите число n: ")
n = input()
r = ""
for i in range(1, len(n)):
    r += n[i]
print("Число х равно:", int(r) * 10 + int(n[0]))
