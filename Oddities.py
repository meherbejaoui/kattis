# 2013 ACM-ICPC North American Qualifier


x = int(raw_input())
for i in range(1,x+1):
    n = int(raw_input())
    if n%2 == 0:
        print '{} is even'.format(n)
    else:
        print '{} is odd'.format(n)