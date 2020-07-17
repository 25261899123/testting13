"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих
соседей и выведите количество таких элементов.(input: 1, 2, 3, 4, 5, output: 0)
"""
list_ = [1, 5, 2, 4, 3, 7, 6, 1, 2, 3, 4, 5]


for lis in range(1, len(list_) - 1):
    string = list_ [lis]
    previus_string = list_[lis-1]
    if list_[lis -1 ] < string > list_[lis+1]:
        print(string)