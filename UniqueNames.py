
import random

# Generate data
names = ['Bill', 'Fred', 'Trevor', 'Kay', 'Helen', 'Beatrice', 'Francoise']
rand_names = []
for i in range(1, 51):
    n = random.randint(0, 6)
    rand_names.append(names[n])

print(rand_names)

uni_names = set(rand_names)

noms = list(uni_names)

print(noms)

# use noms to count each appearance of name in rand_names
print(len(noms))
l = len(noms)
for i in range(0, l):
    print(noms[i], rand_names.count(noms[i]))
