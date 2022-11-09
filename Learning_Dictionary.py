"""
Learning Python Dictionaries

Dictionary Methods
==================
clear
copy
fromkeys
get
items
keys
pop
popitem - he popitem() method removes the item
        that was last inserted into the dictionary
setdefault
update
values
"""

dicts = dir(dict)
methods = []

for i in range(len(dicts)):
    if '__' not in dicts[i]:
        methods.append(dicts[i])

print(methods)

# Datasets

person1 = {"name": "Mary Gallagher",
           "age": 28,
           "profession": "married"}

person2 = {"name": "John Sanin(?)",
           "age": 19,
           "profession": "laborer"}

# Nested Dictionaries

bellevue_people = {
    "person1":
        {"name": "Mary Gallagher",
         "age": 28,
         "profession": "married"},
    "person2":
        {"name": "John Sanin(?)",
         "age": 19,
         "profession": "laborer"}
}

# Keys Method
print(person1.keys())
# Values Method
print(person1.values())
# Items Method
print(person1.items())

# Access Items
print(person1['name'])

# Change a Value
person1['age'] = 100  # e.g change age
print(person1)

# Iterate Through Dictionary
for person in person1.items():
    print(person)

# Copy Method
new_person = person1.copy()
print('Copy:- ', new_person)

# Clear Method
new_person.clear()  # deletes all items in dictionary
print('Empty new_person ', new_person)

# Pop Method - removes the item and returns the value for
# a given key
popped = person1.pop('profession')
print(person1)
print(popped)

# Get Method returns the value if the key exists
# or None if it does not
print(person2)
print(person2.get('age'))
print(person2.get('job'))

# Setdefault Method
# The setdefault() method returns the value of
# the item with the specified key.
# If the key does not exist, insert the key,
# with the specified value, see example below
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)

# The update() method inserts the specified items to the dictionary.
# The specified items can be a dictionary,
# or an iterable object with key value pairs
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)