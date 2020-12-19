n, m = input().split()
mine = []
for i in range(int(n)):
    mine.append([0]*int(m))
k = input()
for p in range(int(k)):
    bn, bm = input().split()
    mine[int(bn)-1][int(bm)-1] = '*'
for j in range(int(n)):
    for l in range(int(m)):
        if mine[j][l] != '*':
            try:
                if mine[j][l+1] == '*':
                    mine[j][l] += 1
            except:
                pass
            try:
                if l-1 >= 0:
                    if mine[j][l-1] == '*':
                        mine[j][l] += 1
            except:
                pass
            try:
                if mine[j+1][l] == '*':
                    mine[j][l] += 1
            except:
                pass
            try:
                if mine[j+1][l+1] == '*':
                    mine[j][l] += 1
            except:
                pass
            try:
                if l - 1 >= 0:
                    if mine[j+1][l - 1] == '*':
                        mine[j][l] += 1
            except:
                pass
            try:
                if j-1 >= 0:
                    if mine[j-1][l+1] == '*':
                        mine[j][l] += 1
            except:
                pass
            try:
                if j - 1 >= 0:
                    if mine[j-1][l] == '*':
                        mine[j][l] += 1
            except:
                pass
            try:
                if j-1 >= 0 and l-1 >= 0:
                    if mine[j-1][l-1] == '*':
                        mine[j][l] += 1
            except:
                pass
for x in range(int(n)):
    for y in range(int(m)):
        print(mine[x][y], end=' ')
    print()
