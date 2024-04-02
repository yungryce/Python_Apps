# fhand = {}
# hands = list()
# fhand['c'] = 1
# fhand['d'] = 10
# fhand['e'] = 4
# print(fhand)
# x = fhand.items()
# print(x)
# for k, v in sorted(fhand.items()):
#     print(v, k)
#     hands.append((v, k))
# hands = sorted(hands, reverse=True)
# print(hands)

# # print(help(sorted))


# fhand = open('romeo.txt')
# agege = dict()
# abule = list()
# for hands in fhand:
#     hands = hands.split()
#     for hand in hands:
#         agege[hand] = agege.get(hand, 0) + 1
# # print(agege)
# for k, v in agege.items():
#     listee = (v, k)
#     abule.append(listee)
# # abule[1] = (5)
# abule = sorted(abule, reverse=True)
# print(abule)
# for v, k in abule[:10]:
#     print(k, v)


# fhand = open('romeo.txt')
# agege = dict()
# abule = list()
# for hands in fhand:
#     hands = hands.split()
#     for hand in hands:
#         agege[hand] = agege.get(hand, 0) + 1
# abule = sorted([(v, k) for k, v in agege.items()], reverse=True)
# print(abule)
# for k, v in abule[:10]:
#     print(k, v)



# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = list()
# for word in words:
#     t.append((len(word), word))
# t.sort(reverse=True)
# print(t)
# res = list()
# for length, word in t:
#     res.append(word)
# print(res)

# import string
# fhand = open('romeo.txt')
# counts = dict()
# for line in fhand:
#     line = line.translate(str.maketrans('', '', string.punctuation)).lower().split()
#     for word in line:
#         counts[word] = counts.get(word, 0) + 1
# # print(counts)
# # Sort the dictionary by value
# lst = list()
# for key, val in counts.items():
#     lst.append((val, key))
# lst.sort(reverse=True)
# # print(lst)

# for key, val in lst[:10]:
#     print(key, val)