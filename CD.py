# Waterloo Programming Contest 2010-09-26


con = True
def process():
    jack = []
    jill = []
    for i in range(n):
        jack.append(int(raw_input()))
    for i in range(m):
        jill.append(int(raw_input()))    
    print len(set(jack)&set(jill))
while con == True:
    n, m = map(int, raw_input().split())
    if (n,m) == (0,0):
        break
    else:
        process()