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

#for x in generate_universal_set(column, n, factor):
#    print(x)

input = "no!yes:low,middle,debtless;average,*,debtless;average,young,indebted;high,*,*"
parts = input.split(':')
target_label = parts[0].split('!')[1] # yes
other_label = parts[0].split('!')[0]  # no
rules = parts[1].split(';')
array = generate_universal_set(column, n, factor)

for element in array:
    found = False
    for rule in rules:
        rule_array = rule.split(',')
        c = 0
        for i in range(num_var_col):
            if rule_array[i] == element[i] or rule_array[i] == '*':
                c = c + 1
        if c == num_var_col:
            element.append(target_label)
            found = True
    if found == False:
        element.append(other_label)

#for element in array:      
#    print(element)

c = 0
for i in range(len(array)):
    for j in range(len(data)):
        if array[i] == data[j]:
            c = c + 1

print("rule accuracy: %f" % (c / len(data)))
