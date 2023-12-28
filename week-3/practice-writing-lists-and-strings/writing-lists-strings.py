# Wk 3 day 3
# PDF worksheet titled: 22-Writing-Lists-1
# Steven Daniel

# Exercise 1    
# Option 1
entered_numbers = []
for i in range(20):
    desired_numbers = eval(input("Please enter 20 numbers of your choosing: " ))
    entered_numbers.append(desired_numbers)
print("Numbers you've entered so far: ", entered_numbers)
print("The average of your numbers is: ", sum(entered_numbers) / len(entered_numbers))

# *****************************************************************************************
# Exercise 2    
# Option 1
def mangle(string):
    string = string.upper()
    string = string[:2] + string[3:] # This removes the 3rd character
    string = string[:-3] + string[-2:] # this removes the 3rd to last character
    return string

print(mangle("hellothere"))
print(mangle("42 degrees Celsius"))
print(mangle("eeeeeee"))

# Solution 
def mangle(str):
    str = str.upper()
    str = str[0:2] + str[3:-3] + str[-2:]
    return str
def main():
    print(mangle("hellothere"))

test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
test_output = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
for i in range(len(test_input)):
    print("Mangle", test_input[i] + ":", mangle(test_input[i]) == test_output[i])

main()
# *****************************************************************************************
# Exercise 3    
def count_e(list):
    num_e = 0 # sum --- aggregates values
    # case insensitive (lower = upper)
    # all strings = loop
    for i in list:
        num_e += i.upper().count("E")
    return num_e
def main():
    print(count_e(["hi", "hello", "EEK!",]))
    print("count_e", count_e(["hi", "hello", "EEK!"]) == 3)

main()

# *******************************************************************************
# Exercise 4     
def count_vowels(list):
    num_vowels = 0
    vowel_list = "AEIOU"
    for string in list:
        upper = string.upper()
        for vowel in vowel_list:
            num_vowels = num_vowels + upper.count(vowel)
    return num_vowels
print(count_vowels(["hi", "hello", "OOF!"]))

# !!!!this was super hard!!!!

# vowels = "A" "a" "E" "e" "I" "i" "O" "o" "U" "u"
# my_vowels = "AaEeIiOoUu"
# count_vowels = ["hi", "hello", "00F!", "AaEeIiOoUu"]
# x = count_vowels.count(vowels)
# print(x)


# def count_vowels(string_list):
#     counter = 0
#     vowels = "AaEeIiOoUu"
#     for string in string_list:
#         if vowels in len(string_list[0]):
#             counter = counter + 1
#             return counter
# print(count_vowels(["hi", "hello", "OOF!"]))


# vowels = "AaEeIiOoUu"
# sentence = "I like bachata", "I like salsa", "I like merengue"
# counter = 0
#
# x = sentence.count(vowels)
# for letter in sentence:
#     counter = counter + sentence.count(vowels)
#     print(letter)
# print(x)
