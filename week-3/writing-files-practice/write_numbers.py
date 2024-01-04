# Week 3 Day 5
# PDF worksheet titled: 23.files.docx
# Steven Daniel

# Exercise 2
# OPTION 1
filename = input("Please enter the name of the file: ")
prompt = "Enter numbers and then enter '0' when finished: "
fileout = open(filename, "w")
response = eval(input(prompt))
while response != 0:
        print(response, file=fileout)
        response = eval(input(prompt))
fileout.close()

# SOLUTION 
list = []
filename = input("Please enter the name of the file: ")
fileout = open(filename, "w")
prompt = "Please enter a number ('0' to finish)"
response = eval(input(prompt))
while response != 0:
    print(response, file=fileout)
    response = eval(input(prompt))

print(sorted(list))
print(sum(list))
print(sum(list)/len(list))

