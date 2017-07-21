# 2016 ICPC North American Qualifier Contest


sen = list(raw_input().lower())
code = {'a':'@', 'b':'8', 'c':'(', 'd':'|)',
'e':'3', 'f':'#', 'g':'6', 'h':'[-]', 'i':'|',
'j':'_|', 'k':'|<', 'l':'1', 'm':'[]\/[]',
'n':'[]\[]','o':'0','p':'|D','q':'(,)','r':'|Z',
's':'$','t':"']['",'u':'|_|','v':'\/','w':'\/\/',
'x':'}{','y':'`/','z':'2'}
res = list()
for i in sen:
    if i in code.keys():
        res.append(code[i])
    else:
        res.append(i)
print ''.join(res)