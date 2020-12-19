r, c = input().split(' ')
if int(c) <= 10:
    direction = "Right"
    seat = c
else:
    direction = "Left"
    seat = 21 - int(c)
row = 11 - int(r)

print(direction+" "+str(row)+" "+str(seat))
