t = input()
ans = []
for i in range(0,int(t)):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    if x == y or x == y+2:
        if x == y == 0:
            duration = 0
        elif x % 2 == 0:
            duration = x+y
        elif x % 2 == 1:
            duration = x+y-1
        else:
            duration = -1
    else:
        duration = -1
    ans.append(duration)
for dr in ans:
    print(dr)

