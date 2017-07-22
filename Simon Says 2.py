# IDI-Open 2015


t = input()
for i in range(t):
    senten = raw_input().split()
    if " ".join(senten[:2]) != "simon says":
        print ''
    else:
        print " ".join(senten[2:])