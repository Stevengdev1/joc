# Wk 3 day 1
# PDF worksheet titled: function-problems
# Steven Daniel

# OPTION 1
def pyramid(text, n):
    for j in range(0, n,):
        for k in range(0, j+1):
            print(text, end="")
        print()

pyramid("m ", 5)

# SOLUTION
def pyramid(char, number):
    for i in range(1, number + 1):
        print(char * i)

def main():
    print('pyramid("*", 20)')
    pyramid("*", 2)

    print('pyramid("+", 5)')
    pyramid("*", 5)

    print('pyramid("x", 10)')
    pyramid("*", 10)

main()