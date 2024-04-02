# z = dict()
# z['juno'] = '1'
# z['zino'] = '1'
# print('juno' in z)
# gege = list(z.values())
# print(gege)

# # for lists
# words = list()
# fhand = open('words.txt')
# for hand in fhand:
#     hand = hand.split()
#     for andd in hand: 
#         if andd not in words:
#             words.append(andd)
# words.sort()
# print(words)



# for dict
from string import punctuation

import string

words = dict()
fhand = open('words.txt')
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    line = line.split()
    for word in line:
    #     words[word] = 1
    # else:
    #     words[word] += 1
        words[word] = words.get(word, 0) + 1
# print(words)
# print(words.get('explain', 0))

highWord = 0
highNum = 0
for aaa, bbb in words.items():
    if bbb > highNum:
        highNum = bbb
        highWord = aaa
print(highWord, highNum)

# # Dict methods: keys(), values(), items()
# lst = list(words.keys())
# lst.sort()
# for key in lst:
#     # print(key, words[key])
#         print(key, words[key])


# {'Fri': 20, 'Thu': 6, 'Sat': 1}
# gege = dict()
# fhand = open('mbox-short.txt')
# for hand in fhand:
#     if not hand.startswith('From '):
#         continue

#     hand = hand.split()
#     hand = hand[2:3]
#     print(hand)
#     for hind in hand:
#         gege[hind] = gege.get(hind, 0) + 1
# print(gege)




# agege = dict()
# highNum = 0
# highWord = 0
# fhand = open('mbox-short.txt')
# for hand in fhand:
#     if not hand.startswith('From '):
#         continue
#     hand = hand.split()
#     hand = hand[1:2]
#     for hind in hand:
#         agege[hind] = agege.get(hind, 0) + 1
# # print(agege)
# for aaa, bbb in agege.items():
#     if bbb > highNum:
#         highNum = bbb
#         highWord = aaa
# print(highNum, highWord)

# agege = dict()
# fhand = open('mbox-short.txt')
# for hand in fhand:
#     hand = hand.rstrip()
#     if not hand.startswith('From:'): continue
#     hand = hand.split('@')
#     hand = hand[1]
#     agege[hand] = agege.get(hand, 0) + 1
# print(agege)


    # hand = hand[1:]
    # for hind in hand:
#         agege[hind] = agege.get(hind, 0) + 1
# print(agege)
