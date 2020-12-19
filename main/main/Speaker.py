n = input()
length = len(n)
length = int(length)
word = []
print(n)
for char in n:
    word.append(char)
for i in range(length-1):
    if i < length - 1:
        for j in range(i+1):
            word[j] = word[i + 1]
    for chars in word:
        print(chars, end='')
    print()
