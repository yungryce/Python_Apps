fhand = open('mbox-short.txt')

leggo = dict()
highNum = 0
highMail = 0

for hand in fhand:
    if not hand.startswith('From '): continue
    hand = hand.split()
    # hand = hand[1]
    print(hand)
#     leggo[hand] = leggo.get(hand, 0) + 1
# print(leggo)


# for aaa, bbb in leggo.items():
#     if bbb > highNum:
#         highNum = bbb
#         highMail = aaa
# print(highMail, highNum)


# for aaa in leggo.values():
#     print(aaa)