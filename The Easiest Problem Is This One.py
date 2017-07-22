# CTU Open 2010


check = True
def process(n):
    return sum(map(int, list(str(n))))
def decide(n):
    pn = process(n)
    m = 11
    while True:
        if process(n*m) == pn:
            return m
        else:
            m += 1
while check :
    n = int(raw_input())
    if n == 0:
        break
    print decide(n)