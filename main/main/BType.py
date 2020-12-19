string = input()
mylist = []
final = []
for i in string:
    mylist.append(i)
for j in mylist:
    if final:
        if j == '=':
            final.pop()
            continue
    if j!= '=':
        final.append(j)
for k in final:
    print(k, end='')
