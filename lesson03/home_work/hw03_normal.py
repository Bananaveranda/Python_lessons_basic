# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fibonacciRow = [1, 1]
    for idx in range(2, m+1):
        a = fibonacciRow[idx-1]+fibonacciRow[idx-2]
        fibonacciRow.append(a)
    fibonacciRow = fibonacciRow[n:m+1]
    return fibonacciRow

print(fibonacci(78,102)) #          счет чисел начинается с нуля

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(spisok):
    for n in range(0, len(spisok)-1):
        for i in range(0, len(spisok)-1-n):
            if spisok[i] > spisok[i+1]:
                spisok[i],spisok[i+1] = spisok[i+1],spisok[i]
    return(spisok)
a = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(a)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

