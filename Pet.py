# Croatian Open Competition in Informatics 2008/2009


winner = 0
points = 0
for i in range(1, 6):
    l = map(int, raw_input().split())
    if sum(l) > points:
        points = sum(l)
        winner = i
print winner, points