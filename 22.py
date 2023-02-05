#Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
#  чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.




#with open('coins.txt', 'r', encoding='utf-8') as f:
#    next(f)
#    a = 0
#    b = 0
#    for i in f:
#        if int(i) == 1:
#            a += 1
#        else:
#            b += 1
#
#print(a if a < b else b)
coins = [1, 0, 1, 1, 0]
print(coins.count(0) if coins.count(0) < coins.count(1) else coins.count(1))


n = int(input())
k = 0
for i in range(n):
    v = int(input())
    if v == 1:
        k += 1
print(k if k<n/2 else n-k)
