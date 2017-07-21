# Southwestern Europe Regional Contest (SWERC) 2015


n, m = map(int, raw_input().split())
pn = 1./n
pm = 1./m
d = {}
for i in range (1,n+1):
    for j in range (1,m+1):
        d[i+j] = d.get(i+j, pn*pm)+pn*pm
lis_of_tup = sorted(d.items(), key=lambda x:x[1])
maxs, maxv = lis_of_tup[len(lis_of_tup)-1]
for i in  (lis_of_tup):
    if i[1] == maxv:
        print i[0]