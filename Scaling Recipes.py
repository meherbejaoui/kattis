# 2015 Rocky Mountain Regional Contest


t = int(raw_input())
for it in range(1, t+1):
    r, p, d = map(int, raw_input().split()) # r: ingredients; p: n of portions for which the recipe is written; d:n of desired portions
    scalingfactor = float(d)/float(p)
    ing = []
    for i in range(r):
        name, weight, percentage = raw_input().split()
        if float(percentage) == 100.:
            main_ing = [[i, name, float(weight)*scalingfactor, float(percentage)]]
        else:
            ing.append([i, name, float(weight), float(percentage)])
    for i in ing:
        i[2] = i[3]*main_ing[0][2]/100
    res = sorted(main_ing+ing)
    print 'Recipe # {}'.format(it)
    for i in res:
        print str(i[1]), "%.1f" % round(i[2],1)
    print '-'*40