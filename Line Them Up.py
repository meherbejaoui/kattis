# 2015 ICPC Mid-Central Regional


n = input()
names = list()
for  i  in xrange(n):
    names.append(raw_input())
if names == sorted(names):
    print "INCREASING"
elif names == sorted(names, reverse=True):
    print "DECREASING"
else:
    print "NEITHER"