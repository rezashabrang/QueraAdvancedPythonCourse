import re

n1 = input()
n2 = input()
n3 = input()
n4 = input()
n5 = input()
answer = []
pattern = "MOLANA|HAFEZ"
if re.search(pattern, n1):
    answer.append(1)
if re.search(pattern, n2):
    answer.append(2)
if re.search(pattern, n3):
    answer.append(3)
if re.search(pattern, n4):
    answer.append(4)
if re.search(pattern, n5):
    answer.append(5)
if answer is None:
    print("NOT FOUND!")
answer.sort()
for ans in answer:
    print(ans, end=" ")
