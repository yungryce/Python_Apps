# import re
# count = 0
# fhand = open('mbox.txt')
# hands = input('Enter a regular expression:')
# for hand in fhand:
#     hand  = hand.rstrip()
#     y = re.findall(hands, hand)
#     if len(y) > 0:
#         count += 1
# print('mbox.txt had', count, 'lines that matched', hands)

# import re
# count = 0
# lst = list()
# fhand = open('mbox-short.txt')
# for hand in fhand:
#     hand = hand.rstrip()
#     y = re.findall('^New Revision: ([0-9]+)', hand)
#     if len(y) > 0:
#         lst.append(int(y[0]))
# a = sum(lst)/len(lst)
# print(a)


import re
count = 0
fhand = open('sum.txt')
for hand in fhand:
    hand = hand.rstrip()
    y = re.findall('([0-9]+)', hand)
    for lint in y: 
        if len(y) > 0: count += int(lint)
print(count)