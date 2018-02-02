import re

handle = open("regex_sum_67903.txt")
#linenum = 0
sum=0

for line in handle:
    #linenum = linenum + 1
    numbers = re.findall('[0-9]+',line)
    #print(linenum, numbers)
    if len(numbers)>0:
        for number in numbers:
            sum = sum + int(number)
            #print(sum)

print (sum)
