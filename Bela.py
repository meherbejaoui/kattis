# Croatian Open Competition in Informatics 2015/2016


n, b = raw_input().split()
dominant = { 'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0 }
non_dominant = { 'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0 }
count = 0
for i in range(4*int(n)):
    card, suit = list(raw_input())
    if suit == b:
        count += dominant[card]
    else:
        count += non_dominant[card]
print count