# CTU Open 2015


tc = int(raw_input())
for i in range(tc):
    n = raw_input()
    nz = 0
    for i in range(1, len(n)+1):
        if int(n)%10**i ==0:
            nz +=1                
    print int(n) - 10**nz