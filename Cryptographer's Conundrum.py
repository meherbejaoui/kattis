# Nordic Collegiate Programming Contest 2015


t = raw_input()
day_count = 0
for i in range(1, len(t)+1):
    if i%3 == 1:
        if t[i-1] != 'P': 
            day_count += 1
    if i%3 == 2:
        if t[i-1] != 'E':
            day_count += 1
    if i%3 == 0:
        if t[i-1] != 'R':
            day_count += 1
print day_count