# Croatian Open Competition in Informatics 2007/2008


inp = map(int, raw_input().split())
shld = [1, 1, 2, 2, 2, 8]
out = list()
for i in range(6):
    out.append(shld[i]-inp[i])
for x in out: print x,