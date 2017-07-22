# Croatian Open Competition in Informatics 2015/2016


l = int(raw_input())
d = int(raw_input())
x = int(raw_input())
def process(n):
    return sum(map(int, list(str(n))))
n, m = 0, 0
for i in range(l, d+1):
    if process(i) == x :
        if n == 0 :
            n = i
            break
for i in range(d,l-1,-1):
    if process(i) == x:
        if m == 0:
            m = i
            break
print n
print m