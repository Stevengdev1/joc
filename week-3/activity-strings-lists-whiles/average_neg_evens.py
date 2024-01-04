# Wk 3 day 4
# PDF worksheet titled: 24.Writing%20Whiles
# Steven Daniel

# OPTION 1
def average_neg_evens(our_list):
    negative_nums = []
    even_nums = []
    i = 0
    while i < len(our_list):
        if our_list[i] < 0:
            negative_nums.append((our_list[i]))
        i = i + 1
        print("this is the negative list: ", negative_nums)
        if negative_nums % 2 == 0:
            print(even_nums)

print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4,]))
print(random_nums[3] % 2 == 0)
print("This is the total of all negative even numbers: ", sum(numbers))
print("This is the total of all negative even numbers: ", sum(numbers) / len(numbers))

# SOLUTION 
def average_neg_evens(list):
    sum = 0
    count = 0
    # print(count)
    for num in list:
        if num < 0 and num % 2 == 0:
            sum = num + 1
            print(sum)
            count = +1  # This increases the count by one every time the loop runs
            print(count)
    return sum / count

print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4,]))

# SOLUTION USING A WHILE LOOP
def average_neg_evens(list):
    sum = 0
    count = 0
    i = 0
    while i < len(list):
        num = list[i]  # This is how we go from index to the value in the list.
        if num < 0 and num % 2 == 0:
            sum = num + 1
            count = +1  # This increases the count by one every time the loop runs
        i = i + 1
    return sum / count

print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4,]))