filename = input("Enter file:")

names = dict()

for line in handle:
    pieces = line.split()
    if len(pieces)!= 0 and pieces[0] == 'From':
        names[pieces[1]] = names.get(pieces[1],0) + 1

#to get the name with the maximum count
maxname = None
maxcount = 0
for name in names:
    if maxname == None or names[name]>maxcount:
        maxname = name
        maxcount = names[name]

print(maxname, maxcount)