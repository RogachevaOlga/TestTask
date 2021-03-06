# Задача 1. Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. Оценить эффективность своего решения.
x = [1, 2, 3, 4, 5]
y = [4, 5, 6, 7, 8, 9, 10]
x_set = set(x)
y_set = set(y)
result = x_set.difference(y_set)
print(result)
# В данной задаче лучше использовать множества.
# Временная сложность операции вычитания множеств x и y: O(длина массива x).

# Задача 2. Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти.
array = [0, 3, 6, 1, 0, 0, 0, 5, 3, 0]
while 1:
    try:
        array.remove(0)
    except:
        break
print(array)
