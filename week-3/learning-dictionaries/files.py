# Week 3 Day 5
# PDF worksheet titled: 23.files.docx
# Steven Daniel

letters = ["A", "B", "C", "D", "F"]
counts = {}
file = "letter-grades.txt"

# I want to loop through all lines in the file.
for line in open(file):
    letter = line.replace("\n", "")  # This replaces the new line with nothing.
    #  if commas, use split function
    # print(line) #  testing
    #  gets the count of letter if it exists,  0 otherwise
    count = counts.get(letter, 0)
    counts[letter] = count + 1  # store count

# Print out counts
print("Letter counts: ")
for l in letters:
    print(l + ":", counts.get(l, 0))
print()

#  Print dictionary
print("File grade counts:")
for item in counts.keys():
    print(item + ":", counts[item])