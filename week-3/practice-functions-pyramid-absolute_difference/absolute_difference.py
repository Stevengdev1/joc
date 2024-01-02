# Wk 3 day 1
# PDF worksheet titled: function-problems
# Steven Daniel


# OPTION 1

# def absolute_difference(par1, par2):
#     return abs(par1 - par2)
#
# print(absolute_difference(200, -200))

# SOLUTION 
def absolute_difference(num1, num2):
    diff = abs(num1 - num2)
    return diff

def main():
    print("difference 5 10",  absolute_difference(5, 10) == 5)
    print("difference 10 5", absolute_difference(10, 5) == 5)
    print("difference 200 -200", absolute_difference(200, -200) == 400)
    print()

main()