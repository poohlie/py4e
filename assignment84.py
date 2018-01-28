fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    pieces = line.split()
    for piece in pieces:
        if piece.lower() not in lst: lst.append(piece.lower())

lst.sort()
print(lst)