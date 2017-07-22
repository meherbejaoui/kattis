# United Kingdom and Ireland Programming Contest 2016


c = float(raw_input())
l = int(raw_input())
total = []
for i in range(l):
    a, b = map(float, raw_input().split())
    total.append(c*a*b)
print '%.7f'  % sum(total)