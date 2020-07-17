"""
18.Циклически сдвиньте элементы списка вправо (A[0] переходит на место
A[1], A[1] на место A[2], ..., последний элемент переходит на место
A[0]). Используйте минимально возможное количество операций
присваивания.(input: 1, 2, 3, 4, 5 output: 5, 1, 2, 3, 4)
"""
nums = [1,2, 3, 4, 5, 6, 7]
lst = nums
steps = -6
if steps < 0:
    steps = abs(steps)
    for i in range(steps):
        lst.append(lst.pop(0))
else:
    for i in range(steps):
        lst.insert(0, lst.pop())
lst = nums
print(nums)