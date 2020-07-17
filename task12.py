"""
12.Выведите значение наименьшего нечетного элемента списка, а если в
списке нет нечетных элементов - выведите число 0.(input: 0, 1, 2, 3, 4
output: 1)
"""
list_ = [2,3,4,5,6,7,8,9,10,11,12]
list_new = []
for num in list_:
    if num % 2 != 0:
        list_new.append(num)

min_= min(list_new)
print(min_)