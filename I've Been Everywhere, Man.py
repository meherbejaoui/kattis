# 2015 Rocky Mountain Regional Contest


t = int(raw_input())
for i in range(t):
    s = set()
    for i in range(int(raw_input())):
        s.add(raw_input())
    print len(s)