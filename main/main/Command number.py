def solve(path):
    import re
    counter = 0
    with open(path, "r+") as f:
        while True:
            line = f.readline()
            if line == '':
                break
            else:
                if re.search('[\s*]#', line) or line == '\n' or re.match("^\s*$", line):
                    continue
                elif re.match('[\d\w\s]', str(line)):
                    counter += 1
    return counter


print(solve("file.txt"))
