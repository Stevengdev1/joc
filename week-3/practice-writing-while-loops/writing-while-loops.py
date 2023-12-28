# Wk 3 day 4
# PDF worksheet titled: 23.WritingWhiles
# Steven Daniel

# Exercise #1a
    # Option 1
count = 0
while count < 6:
    print(count)
    count += 1

    # Solution
i = 1
while i <= 5:
    print(i)
    i += 1

# Exercise #1b
    # Option 1
count = 2
while count < 12:
    print(count)
    count += 3

    # Solution 
x = 2
while x < 12:
 print(x)
 x += 3

# Exercise #1c
    # Option 1
count = -10
while count < 1:
    print(count, end=" ")
    count += 2
    print()

    # Solution 
y = -10
while y <= 0:
    print(y, end=" ")
    y += 2
    print()

# Exercise #1d
    # Option 1
count = 0
while count < 4:
    print("****")
    count += 1

    # Solution
z = 0
while z < 4:
 print(4 * "*")
 z += 1

# *****************************************************************************************
 
# Exercise 2
    # Option 1
phrase = "CSCI 150"
count = 0
while count < len(phrase):
    print(phrase[count])
    count += 1

    # Solution 
string = "CSCI 150"
i = 0
while i < len(string):
 print(string[i])
 i += 1
 # (I got everything right, except the [count] part so that it
 # prints each character individually)

# *****************************************************************************************

# Exercise 3
    # Option 1
number_list = []
number_request = ("continue entering numbers, enter the number 0 when finished: ")
numbers_entered = eval(input(number_request))
while numbers_entered != 0:
    number_list.append(numbers_entered)
    numbers_entered = eval(input(number_request))
print("The numbers you've entered are: ", sorted(number_list))
print("The sum of all your numbers is: ", sum(number_list))
print("The sum of all your numbers is: ", sum(number_list) / len(number_list))

    #Solution 
list = []
prompt = "Please enter a number ('0' to finish)"
response = eval(input(prompt))
while response != 0:
    list.append(response)
    response = eval(input(prompt))
print(sorted(list))
print(sum(list))
print(sum(list)/len(list))