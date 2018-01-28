fname = input("Enter file name: ")

fh = open(fname)
count = 0

for line in fh:
    pieces = line.split()
    if len(pieces)!=0:
        if pieces[0] == 'From':
            count = count+1
            print(pieces[1])

print('There were '+str(count)+' lines in the file with From as the first word')
