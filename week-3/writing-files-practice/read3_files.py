# Week 3 Day 5
# PDF worksheet titled: 23.files.docx
# Steven Daniel

# Exercise 3

def count_lines(filename):
    total = 0
    for line in open(filename):
        total += 1
    return filename + " : " + str(total)
list = ["text1.txt", "text2.txt", "text3.txt"]
send_files = open("counts.txt", "w")
for file in list:
    print(count_lines(file), file=send_files)
send_files.close()
