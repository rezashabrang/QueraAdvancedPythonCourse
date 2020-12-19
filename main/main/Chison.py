import json
import re
import ast
n = input()
commands = []
i = 1
while int(i) <= int(n):
    line = input()
    commands.append(line)
    i += 1
for j in commands:
    if re.search(":=", j):
        string = j.split(':=')
        primvar = string[0]
        var = str(primvar).rstrip()
        primaryValue = string[1]
        value = str(primaryValue).lstrip()
        finalString = var + '=' + value
        exec(finalString)
    elif re.match("print", j):
        zprint = j.split(' ')
        wprint = str(zprint[1]).split('[')
        var = wprint[0]
        vprint = str(wprint[1]).split(']')
        index = vprint[0]
        exec("print(" + var + '[' + index + ']' + ')')
