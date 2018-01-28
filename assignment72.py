fname = input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    else:
        #print(line)
        total = total + float(line[line.find('0'):])
        count = count + 1

average = total/count
print("Average spam confidence: "+str(average))