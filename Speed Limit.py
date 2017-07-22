# 2004 ACM ICPC Mid-Central North American Regional Contest


while True:
    t = int(raw_input())
    if t == -1:
        break
    else:
        speed, time = [], []
        t_old = 0
        for i in range(t):
            s, t = map(int, raw_input().split())
            speed.append(s)
            time.append(t-t_old)
            t_old = t
        print sum([x*y for x,y in zip(speed, time)]), 'miles'