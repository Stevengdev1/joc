# Week 3 Day 5
# PDF worksheet titled: 23.files.docx
# Steven Daniel
#  Exercise 1

#  OPTION 1
file = "text-file1.txt"
# looping through all the lines in the file
for line in open(file):
    phrase = line.replace("\n", "")
    print("-"+phrase)

# SOLUTION 

dataIn = open('text-file1.txt')
for line in dataIn:
    print("-", line.rstrip())
dataIn.close()
