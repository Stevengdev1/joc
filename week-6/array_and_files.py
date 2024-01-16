# Week 6 Day 1
# PDF worksheet titled: day-1-Activity-Arrays-Files.pdf
# Steven Daniel

file = open("turing.txt")
line_array = []
# print("This is the line_array: ", line_array)
for line in file:
    line_array.append(line.rstrip())
file.close()
print("This is the first line: ", line_array[0])
print("This is the last two elements of the array: ", line_array[-2:]) 
print("The number of lines in my file are: ", len(line_array))
