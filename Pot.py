# Croatian Open Competition in Informatics 2015/2016


N = input()
X = 0
for i in range(N):
    numb = input()
    p = int(list(str(numb))[len(str(numb))-1])
    r = (numb - p) / 10
    X += (r**p)
print X