def calc(inp=[]):
    sums = 0
    n = 0
    maxi = 0
    inp = sorted(inp, reverse=True)
    for i in inp:
        sums += i
        n += 1
    ave = float(sums/n)
    maxi = max(inp)
    if n % 2 == 0:
        mid = float((inp[int((n/2)-1)]+inp[int(n/2)])/2)
    else:
        mid = int(inp[int((n+1)/2)-1])
    answer = (ave, mid, maxi)
    return answer
