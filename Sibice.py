# Croatian Open Competition in Informatics 2006/2007


from math import sqrt
n, w, h = map(int, raw_input().split())
x = sqrt(w**2 + h**2)
for i in xrange(n):
    if int(raw_input()) <= x:
        print 'DA'
    else:
        print 'NE'