# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
list_random = [random.randint(1,10) for i in range(10)]
list_sqrt = [i**2 for i in list_random]
print(list_sqrt, list_random)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

a = ['apple', 'orange', 'banana', 'kiwi', 'mango']
b = ['grape', 'pear', 'orange', 'banana', 'pineapple']
double_list = [i for i in a for j in b if i==j]
print(double_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
list_random = [random.randint(1,10) for i in range(10)]
list_direct = [i for i in list_random if i % 3 == 0 and i >= 0 and i % 4 != 0]
print(list_direct, list_random) 
