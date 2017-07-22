# 2015 ICPC Mid-Central Regional


def val(password, message):
    pos = 0
    for j in range(len(password)):
        pos = min([message.find(c, pos) for c in password[j:] ])
        if (message[pos] != password[j]) or (pos == -1):
            return False
        pos += 1
    return True
password, message = raw_input().split()
res = val(password, message)
if res:
    print 'PASS'
else:
    print 'FAIL'