# Week 3 Day 5
# PDF worksheet titled: "23.files.docx"
# Steven Daniel
# Exercise 4


list = ["text1.txt", "text2.txt", "text3.txt"]
send_files = open("counts.txt", "w")
total_lines = 0
total_words = 0
for file in list:
    lines = 0
    words = 0
    for line in open(file):
        lines += 1
        words += len(line.split(" "))
    total_lines += lines
    total_words += words
    print(file, " : ", lines, "lines,", words, "words", file=send_files)
print("TOTAL:", total_lines, "lines,", total_words, "words", file=send_files)
send_files.close()