n = input()
names = []
fn = []
ln = []
hats = 1
for i in range(int(n)):
    names = str(input()).split()
    fn.append(names[0])
    ln.append((names[1]))
firstnames =set(fn)
for word in firstnames:
    count = 0
    for i in fn:
        if word == i:
            count += 1
    if count > hats:
        hats = count
print(hats)