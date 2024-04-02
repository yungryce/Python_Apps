# fhand = open('mbox.txt')
# counts = dict()
# lst = list()
# for hand in fhand:
#     if hand.startswith('From '):
#         hand = hand.split()
#         line = hand[1]
#         counts[line] = counts.get(line, 0) + 1
# # print(counts)
# for email, count in counts.items():
#     combined = count, email
#     lst.append(combined)
# lst.sort(reverse=True)
# print(lst)


# fhand = open('mbox-short.txt')
# counts = dict()
# lst = list()
# for hand in fhand:
#     if hand.startswith('From '):
#         hand = hand.split()
#         word = hand[5]
#         time = word.split(':')
#         ade = time[0]
#         counts[ade] = counts.get(ade, 0) + 1

# for a, b in counts.items():
#     listee = (a, b)
#     lst.append(listee)
# lst.sort()
# print(lst)
# for timee, countee in lst:
#     print( timee, countee)