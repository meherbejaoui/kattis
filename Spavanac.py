# Croatian Open Competition in Informatics 2009/2010


h, m = map(int, raw_input().split())
t = h*60 +m
newt = t-45
if h == 0:
    nh = 23
else:
    nh = newt//60
nm = newt%60
print nh,nm