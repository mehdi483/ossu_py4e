# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the number

import re

fileHandler = open("regex_sum_1210180.txt")
fileNumbers = list()

for line in fileHandler:
    lineNumbers = re.findall("[0-9]+", line)
    for number in lineNumbers:
        fileNumbers.append(int(number))

print(sum(fileNumbers))