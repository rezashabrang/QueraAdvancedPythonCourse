userlist = []
albumlist = []
answerlist = []
n = input()
for items in n:
    userdic={}
    for counter in range(3):
        line = input()
        line = line.split(':')
        attr = line[1].strip()
        userdic[getuserattr(counter)] = attr
    userlist.append(userdic)
m = input()
for items in m:
    albumdic={}
    for counter in range(3):
        line = input()
        line = line.split(':')
        attr = line[1].strip()
        albumdic[getalbumarrt(counter)] = attr
    albumlist.append(albumdic)

def getalbumarrt(counter):
    if counter == 0:
        return 'name'
    elif counter == 1:
        return 'singer'
    elif counter == 2:
        return 'genre'
    elif counter == 3:
        return 'tracks'

def getuserattr(counter):
    if counter == 0:
        return 'name'
    elif counter == 1:
        return 'age'
    elif counter == 2:
        return 'city'
    elif counter == 3:
        return 'albums'




