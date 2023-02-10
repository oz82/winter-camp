from pathlib import Path
file_path = Path(__file__).parent.parent.joinpath('data/credit.txt')

def generate_universal_set(column, n, factor):
    result = []
    # enumeration
    for i in range(n):
        balance = i
        array = []
        for j, f in enumerate(factor):
            quotient = int(balance / f)
            #print("%d - %d - %d" % (i, f, quotient))
            array.append(column[j][quotient])
            balance = balance - quotient * f
        result.append(array)
    return result

f = open(file_path, "r")
lines = f.read().splitlines()
num_row = len(lines) - 1
for line in lines:
    if line.startswith('#'):
        num_col = len(line[1:].split('\t'))
        break

num_var_col = num_col - 1
data = []
title = []
column = []
sets = [set() for i in range(num_var_col)]

for line in lines:
    if line.startswith('#'):
        title = line[1:].split('\t')
        continue
    values = line.split('\t')
    data.append(values)
    for i in range(num_var_col):
        sets[i].add(values[i])

n = 1
for a_set in sets:
    column.append(list(a_set))
    n = n * len(a_set)

factor = [0] * num_var_col
temp = 1
for i in reversed(range(1, num_var_col)):
    temp = temp * len(column[i])
    factor[i - 1] = temp
factor[len(factor)-1] = 1

#print(factor)
#print(n)
#print(column)
#print()
#print(data)
#print(column[0].index('high'))

for x in generate_universal_set(column, n, factor):
    print(x)