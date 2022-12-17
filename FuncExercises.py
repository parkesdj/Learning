# Write a program to create a function that takes two arguments, name and age, and print their value.
def person(name, age):
    print(f'Name: {name}  Age: {age}')

person('David', 68)

# In Python, to return multiple values from a function, use a comma to separate them.
def func1(*args):
    for i in args:
        print(i)

func1(1, 4, 7, 8)
# Write a program to create function calculation() such that it can accept two variables
# and calculate addition and
# subtraction. Also, it must return both addition and subtraction in a single return call.
def calculation(a, b):
    res = a + b, a - b
    print(res)

calculation(40, 10)

# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name, salary=9000):
    print(name, salary)

show_employee('John', 7860)


