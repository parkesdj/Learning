"""
This a tutorial on List, Tuples and Sets
"""
# Lists

courses = ['History', 'Maths', 'Physics', 'CompSci']

print(courses)
print(len(courses))

# Lists indexing and slicing
for i in range(len(courses)):
    print(courses[i])
print()
# Using negative indices
print(courses[-1])
# From end or beginning
print(courses[2:])
print(courses[:3])

# List methods
courses.append('Art')
print(courses)

courses.insert(2,'Geography')
print(courses)

courses_2 = ['Chemistry', 'Technology']
# Insert adds new list as a separate list
courses.insert(0, courses_2)
print(courses)
# Extend adds list as list items
courses.extend(courses_2)
print(courses)

# Remove items
print('Removing')
courses.remove('CompSci')
print(courses)

# Pop item removes last item in list
print('Popping')
popped = courses.pop()
print('Popped Item:',popped)
print(courses)

# Sorting Lists
names = ['Brian', 'Alfred', 'Cyril', 'Cuthbert', 'Desmond']
nums = [3,8,2,7,5]
print('Reversing')
courses.reverse()
print(courses)
print('Sorting Alpha and Numeric')
names.sort()
nums.sort()
print(names)
print(nums)
# Sorting in reverse order
print('Sorting in reverse order')
names.sort(reverse=True)
nums.sort(reverse=True)
print(names)
print(nums)

# Sorting without sorting original list
trees = ['oak','elm','ash', 'beech', 'willow', 'aspen','maple']
sorted_trees = sorted(trees)
print(trees)
print(sorted_trees)

# Min, Max, Sum
print('Minimum',min(nums))
print('Maximum', max(nums))
print('Sum', sum(nums))

# Find index
print(names.index('Cuthbert'))
print('Fred' in names) # check if in list to avoid error

# Looping using enumerate
for index, item in enumerate(names):
    print(index, item)

# List to string
name_string = ', '.join(names)
print(names)
print(name_string)
# String to list
new_list = name_string.split(',')
print(new_list)