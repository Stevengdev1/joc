# Week 3 Day 5
# (No worksheet) Lesson is titled: Day 5: Learning Activity: Data Project Practice
# by Steven Daniel
# Data Project Practice using provided sample_grades.csv

import statistics
def output_stats(list):
    print("Mean:   ", statistics.mean(list))
    print("Median: ", statistics.median(list))
    print("STD:    ", statistics.mean(list))
    print()

spring = []
fall = []

csv = "sample_grades.csv"
file = open(csv)
for line in file:
    # print(line.rstrip())
    list = line.rstrip().split(",")
    # print(list)
    if list[1] == "Spring 2016":
        spring.append(eval(list[2]))
    else:
        fall.append(eval(list[2]))
file.close()

print("Fall 2016:")
output_stats(fall)
print("Spring 2016:")
output_stats(spring)


