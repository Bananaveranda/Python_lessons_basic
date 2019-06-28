# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
#python2
fruits = ["яблоко", "банан", "киви", "арбуз"]
for idx, itm in enumerate(fruits, start=1):
    print('{}. {:>10}'.format(idx, itm))
    
    
#python3
fruits = ["яблоко", "банан", "киви", "арбуз"]
max_len = len(max(fruits))
i = 0
while i <len(fruits):
    print(f'{i+1}.{fruits[i],rjust(max_len," ")}')
    i+=1
    
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

          import random
list_1 = []
for i in range(10):
    element = random.randint(1,10)
    list_1.append(element)
list_2 = []
for i in range(10):
    element = random.randint(1,10)
    list_2.append(element)
new_list = []
i = 0
while i < len(list_2):
    if not list_1[i] in list_2:
        new_list.append(list_1[i])
    i+=1
print('{} уникальный список из {}, очищенный от списка {}'.format(new_list, list_1, list_2))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
