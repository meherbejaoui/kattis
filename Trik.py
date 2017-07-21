# Croatian Open Competition in Informatics 2006/2007


t = map(str.lower, raw_input())
p = 1
for i in t:
    if i == 'a' and p != 3:
        p = 3 - p
    elif i == 'b' and p != 1:
        p = 5 - p
    elif i == 'c' and p != 2:
        p = 4 - p
print p