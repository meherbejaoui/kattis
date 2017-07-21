# Croatian Open Competition in Informatics 2007/2008


xlst = []
ylst = []
for i in range(3):
    x, y = map(int, raw_input().split())
    if x in xlst :
        xlst.remove(x)
    else:
        xlst.append(x)
    if y in ylst:
        ylst.remove(y)
    else:
        ylst.append(y)
print xlst[0], ylst[0]