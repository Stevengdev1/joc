# Wk 3 day 4
# PDF worksheet titled: 24.Writing%20Whiles
# Steven Daniel

# OPTION 1
def count_letter(list, letter):
    count = 0
    letter = letter.lower()  # We lower-case the letter here so that it lower-cases
                            # every string in our letter parameter
    for string in list:
        count = count + string.lower().count(letter)
    return count #the number of times this letter occurs, both upper- & lower-cased.

list = ["HELLO", "goodbye", "1234 Oooh!"]
print(count_letter(list, "o"))

# SOLUTION USING WHILE LOOP
def count_letter(list, letter):
    count = 0
    letter = letter.lower()  # We lower-case the letter here so that it lower-cases
    i = 0                       # every string in our letter parameter
    while i < len(list):
        string = list[i]
        count = count + string.lower().count(letter)
        i = i + 1
    return count #the number of times this letter occurs, both upper- & lower-cased.

list = ["HELLO", "goodbye", "1234 Oooh!"]
print(count_letter(list, "o"))