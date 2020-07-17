"""
19.В списке все элементы различны. Поменяйте местами минимальный и
максимальный элемент этого списка.(input: 3, 4, 5, 2, 1 output: 3, 4, 1, 2,
5)
"""
list_ = [3, 4, 5, 2, 1, 6, 7, 5, 19]


min_= min(list_)
max_= max(list_)


min_1 = list_.index(min_)
max_1 = list_.index(max_)
print(min_1)
print(max_1)

list_[min_1]= max_
list_[max_1]= min_

print(list_)