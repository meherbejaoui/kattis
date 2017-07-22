# Croatian Open Competition in Informatics 2007/2008


a, b, c = map(int, raw_input().split())
if a+b == c: print '%d+%d=%d' % (a,b,c)
elif a-b == c: print '%d-%d=%d' % (a,b,c)
elif a*b == c: print '%d*%d=%d' % (a,b,c)
elif a/b == c: print '%d/%d=%d' % (a,b,c)
elif b+c == a: print '%d=%d+%d' % (a,b,c)
elif b-c == a: print '%d=%d-%d' % (a,b,c)
elif b*c == a: print '%d=%d*%d' % (a,b,c)
elif b/c == a: print '%d=%d/%d' % (a,b,c)