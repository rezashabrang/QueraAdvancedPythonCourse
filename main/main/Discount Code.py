import re


def removeDuplicate(str, n):
    # Used as index in the modified string
    index = 0

    # Traverse through all characters
    for i in range(0, n):

        # Check if str[i] is present before it
        for j in range(0, i + 1):
            if (str[i] == str[j]):
                break

        # If not present, then add it to
        # result.
        if (j == i):
            str[index] = str[i]
            index += 1

    return "".join(str[:index])


def ans(answers):
    for answ in answers:
        print(answ)


n, t = input().split(" ")
subsetString = removeDuplicate(list(t), len(t))
listSubset = []
answers = []
for char in subsetString:
    listSubset.append(char)
listSubset.sort()
for codes in range(int(n)):
    code = input()
    codeString = removeDuplicate(list(code), len(code))
    listCode = []
    for ch in codeString:
        listCode.append(ch)
    listCode.sort()
    if listCode == listSubset:
        answers.append("Yes")
    else:
        answers.append("No")

ans(answers)
