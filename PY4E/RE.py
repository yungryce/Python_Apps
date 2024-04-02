# import re

# words = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# # word = words.split()
# # email = word[1]
# # piece1, piece2 = email.split('@')
# # print(piece2)

# y = re.findall([])


# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From:.+@', line):
#         print(line)

# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('\S+@\S+', line)
#     if len(x) > 0:
#         print(x)



# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('^X\S*: ([0-9.]+)', line)
#     if len(x) > 0:
#         print(x)

# hand = open('mbox-short.txt')
# import re
# for hands in hand:
#     hands =  hands.rstrip()
#     y = re.findall('^Details:.*=([0-9]+)', hands)
#     if len(y) > 0:
#         print(y)

# fhand = open('mbox-short.txt')
# import re
# for hands in fhand:
#     hands = hands.rstrip()
#     y = re.findall('^From .* ([0-9][0-9]:.*)\s', hands)
#     if len(y) > 0:
#         print(y)


