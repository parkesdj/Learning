"""
Learning Python Sets
"""

setz = dir(set)
for i in range(len(setz)):
    if '__' not in setz[i]:
        print(setz[i])

names = {'Kevin', 'Jane', 'Cedric', 'Malcolm', 'Adam', 'Jane'}
names2 = {'Kevin', 'George', 'Clarence', 'Malcolm', 'Scott', 'Jane'}
# Sets are un ordered. Duplicates are automatically removed (see Jane)
print(names)
# Membership Test
print('Cedric' in names)
# Intersection Method
print('Intersection')
print(names.intersection(names2))
print('Difference names to names2')
print(names.difference(names2))
print('Difference names2 to names')
print(names2.difference(names))

# Union Method
print(names.union(names2))

# Add Method
names.add('Gladys')
print(names)

# Clear Method removes all values
print('---------')
names.clear()
print(names)
print('--------')
names.add('Sebastian')
print(names)