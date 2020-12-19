mylist = []
x = 1
while True:
    x = input()
    if int(x) == 0:
        break
    mylist.append(x)
i = -1
while int(i)>=-len(mylist):
    print(mylist[i])
    i = i -1