"""
Learning tutorial Tuples

Tuples are  immutable
METHODS
-------
count
index
"""
t = dir(tuple)
tuple_methods = ''

for i in range(len(t)):
    if '__' not in t[i]:
        tuple_methods = tuple_methods + ' ' + (t[i])
print('Tuple Methods are: ', tuple_methods)

names = ('Cuthbert', 'Adam', 'Zac', 'Derek', 'Johnathan', 'Zac', 'Abagail')

# Count Method - how many times a value appears in list
print(names.count('Zac'))

# Index Method - finds the index of the first appearance of target value
print(names.index('Zac'))

# Index Method - using 'value', start index, stop index (assumes beginning or end if left blank)
print(names.index('Zac', 3,))
