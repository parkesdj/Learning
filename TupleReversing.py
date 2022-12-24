"""
Reverse order of a tuple
"""
tuple1 = (10, 20, 30, 40, 50)

new_list = []

for i in range(4, -1, -1):
    new_list.append(tuple1[i])
del tuple1
tuple1 = tuple(new_list)
print('new tuple', tuple1)

