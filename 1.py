# Задача 1: Найдите сумму цифр трехзначного числа.
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)
print('введите трехзначное число: ')
a = int(input())
c = a % 10
b = a % 100 // 10
a = a // 100
print(c + b + a)