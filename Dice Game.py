# Nordic Collegiate Programming Contest 2014


gunnar = map(int, raw_input().split())
emma = map(int, raw_input().split())

if  sum(gunnar) > sum(emma) :
    print 'Gunnar'
elif sum(gunnar) < sum(emma):
    print 'Emma'
else:
    print 'Tie'