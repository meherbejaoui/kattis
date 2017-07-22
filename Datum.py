# Croatian Open Competition in Informatics 2008/2009


d, m = map(int, raw_input().split())
m31 = [1,3,5,7,8,10,12]
m30 = [4, 6, 9, 11]
m28 = [2]
tot = d
for i in xrange(1,m):
    if i in m31:
        tot += 31
    elif i in m30:
        tot += 30
    else:
        tot += 28
res = tot % 7
week = {'1':'Thursday', '2':'Friday', '3':'Saturday', '4':'Sunday',
        '5':'Monday', '6':'Tuesday', '0':'Wednesday'}
print week[str(res)]