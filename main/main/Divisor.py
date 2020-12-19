def divs(a):
    l = 1
    while l < a+1:
        if a % l ==0:
            yield l
        l += 1

for i in divs(10):
    print(i)