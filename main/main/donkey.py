import math
a, b, l = input().split()
# res = xa + yb
# x + y = l
res = int(math.ceil(int(l)/2)*int(a))+int(math.floor(int(l)/2)*int(b))
print(res)