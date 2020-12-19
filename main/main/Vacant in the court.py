import re

inp = str(input())
inp = inp.split(" + ")
num1 = inp[0]
inp = inp[1].split(" = ")
num2 = inp[0]
res = inp[1]

def check(inp, number):
	inp = inp.split("#")
	start = inp[0]
	end = inp[1]
	pattern = ""
	if len(start) != 0:
		pattern = pattern + "^" + start
	pattern = pattern + ".*"
	if len(end) != 0:
		pattern = pattern + end + "$"
	find = re.search(pattern,number)
	if find != None:
		return True
	return False

if '#' in num1:
	if check(num1,str(int(res)-int(num2))):
		print((int(res)-int(num2))," + ",num2," = ",res)
	else:
		print("-1")
elif '#' in num2:
	if check(num2,str(int(res)-int(num1))):
		print(num1," + ",(int(res)-int(num1))," = ",res)
	else:
		print("-1")
else:
	if check(res,str(int(num1)+int(num2))):
		print(num1," + ",num2," = ",(int(num1)+int(num2)))
	else:
		print("-1")