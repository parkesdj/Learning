"""
Learning Python Sets
Methods:-
add <-
clear <-
copy <-
difference <-
difference_update <-
discard <-
intersection <-
intersection_update <-
isdisjoint ->>>> check whether the two sets are disjoint
or not, if it isdisjoint then it returns True otherwise
it will return False.
issubset <-
issuperset <-
pop ->>> randomly removes an item from the set
remove < -
symmetric_difference
symmetric_difference_update
union <-
update <-
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

# Intersection Update Method - removes item(s) that does not
# appear in both lists
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print('Intersection_update result:- ', x)

# Intersection Method
print('Intersection')
print(names.intersection(names2))
print('Difference names to names2')

# Difference Method
print(names.difference(names2))
print('Difference names2 to names')
print(names2.difference(names))

# Copy
print('Copy of names set:', names.copy())

# Union Method
print(names.union(names2))

# Add Method
names.add('Gladys')
print(names)

# Update Method - add multiple items from iterable object
# e.g. List to set
new_names = ['Rupert', 'Rachael', 'Ivan']
names.update(new_names)
print('Updated Set: ', names)

# Clear Method removes all values
print('---------')
names.clear()
print(names)
print('--------')
names.add('Sebastian')
print(names)

# Difference Update Method - Remove the items that exist in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)
print(x)

# Discard Method - unlike remove() discard() does not raise an
# error if the item is not in the list
# Remove "banana" from the set:

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

# Union Method - The union() method returns a set that
# contains all items from the original set,
# and all items from the specified set(s) or other iterable.

w = ('u', 'v', 'x')
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(w, y, z)

print('Unified set: ', result)

# Issubset Method - returns True if set b is a subset of
# set a

a = {'q', 'w', 'e', 'r', 't', 'y'}
b = {'w', 'e', 'r'}

m = b.issubset(a)
print(m)

# Issuperset Method -  returns True if all items in
# set b are in set a

a = {'q', 'w', 'e', 'r', 't', 'y'}
b = {'w', 'e', 'r'}

m = a.issuperset(b)
print(m)