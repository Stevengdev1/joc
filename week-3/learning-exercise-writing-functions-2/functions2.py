# Wk 3 day 2
# PDF worksheet titled: 07.LE-WritingFunctions2
# Steven Daniel
# *******************************************************************

# Exercise 4
def is_even(number):
    return number % 2 == 0

def main():
    print("44 is an even number:", is_even(44))
    print("55 is an odd number:", is_even(55))
main()

# *******************************************************************

# Exercise 5
import math
# option 1
# def calculate_total(meal, tax_rate, tip_rate):
#     return tip_amount = (meal * tip_rate)
#     total_amount = (meal * tax_rate) + tip_amount
#     print(float(tip_amount))
#     print(total_amount)
# calculate_total(53.48, 0.07, 0.18)


# Solution
def calculate_total(meal, tax_rate, tip_rate):
    tip = meal * tip_rate
    tax = meal * tax_rate
    return meal + tip + tax
print(calculate_total(53.48, 0.07, .18))

# *********************************************************************

# Exercise 6
# def hey(num):
#     return num * num
#
# print(hey(5))
# print(hey(0))
# print(hey(-3))

# Solution
def hey(num):
    return num ** 2

print(hey(5))
print(hey(0))
print(hey(-3))

# *********************************************************************

#Exercise 7
# Option 1
# def there(n):
#     if n > 2:
#         print(2 ** n)
#     elif n < 2:
#         print(0)
#
# there(5)
# there(0)
# there(3)
# there(-2)
# there(-6)

# Solution
def there(num):
    if num < 0:
        return 0
    #else: this is optional( when adding the keyword return, the function automatically ends)
    return 2 ** num

print(there(5) == 32)
print(there(0) == 1)
print(there(3) == 8)
print(there(-2) == 0)
print(there(-6) == 0)

# *******************************************************************

# Exercise 8
# Option 1
def are_we(no_times, phrase):
    for i in range(0, no_times):
        print("Are we", phrase, "yet?")

are_we(2, "there")
are_we(3, "50")
are_we(1, "")
are_we(0, "hey!")

# Solution
def are_we(no_times, phrase):
    for i in range(0, no_times):
        print("Are we", phrase, "yet? ", end="")
    print()

are_we(2, "there")
are_we(3, "50")
are_we(1, "")
are_we(0, "hey!")