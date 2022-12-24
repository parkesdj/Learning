even_nums = []

def evens(num) :
    for i in range(4, num + 1):
        # print(i)
        if i % 2 <= 0:
            even_nums.append(i)
    print(even_nums)


evens(30)
