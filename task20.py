"""
20.Дан список из чисел и индекс элемента в списке k. Удалите из списка
элемент с индексом k, сдвинув влево все элементы, стоящие правее
элемента с индексом k. Программа получает на вход список, затем число
k. Программа сдвигает все элементы, а после этого удаляет последний
элемент списка при помощи метода pop(). Программа должна
осуществлять сдвиг непосредственно в списке, а не делать это при
выводе элементов. Также нельзя использовать дополнительный
список.(input: 7, 6, 5, 4, 3, 2, 1, 2 output: 7, 6, 4, 3, 2, 1)
"""

list_ = [7, 6, 5, 4, 3, 2, 1, 2]
print("Введите index:")
k = int(input())

for num in range(len(list_)-1) :
    if k == list_[num]:
        list_.pop(list_[num])
for num in range(len(list_)-1) :
    if k == 0:
        list_.pop(0)
        break
list_.pop()
print(list_)
