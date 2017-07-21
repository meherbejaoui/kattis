# 2015 ICPC North American Qualifier Contest


n = input()
for i in range(n):
    sent = raw_input().split()
    if " ".join(sent[:2]) != "Simon says":
        continue
    else:
        out = " ".join(sent[2:]) 
    print out