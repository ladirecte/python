#Задача 1. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
#Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
#Input: 5 -> 5 1 6 5 9
#Output: 1 9


print('введите кол-во арбузов: ')
num = int(input())

print('введите вес арбузов: ')

cur_wmelon = int(input())
min_wmelon = max_wmelon = cur_wmelon
input_numbers = str(cur_wmelon)

for i in range (2, num + 1):
    cur_wmelon = int(input())
    input_numbers += "" + str(cur_wmelon)
    if min_wmelon > cur_wmelon:
        min_wmelon = cur_wmelon
    elif max_wmelon < cur_wmelon:
        max_wmelon = cur_wmelon

print("Input:", num, "->", input_numbers)
print("Output:", min_wmelon, max_wmelon)
