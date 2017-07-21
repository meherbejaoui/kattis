# Croatian Open Competition in Informatics 2006/2007


rl = list()
for i in range(1,11):
    n = int(raw_input())
    rl.append(n)
l = map(lambda x:x%42, rl)
print len(set(l))