"""
x = 'Joy'
# print(dir(x))

stuff = list()
stuff.append('Girl')
stuff.append('boy')
stuff.append(x)
# stuff.append(4)
print(9 in stuff)
print(9 not in stuff)
print(stuff)
stuff.sort() #sorts alphabethically. upper > lower
print(stuff)
"""

# count = 0
# total = 0
# while True:
#     inp = input('Please insert number:')
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1
# a = total/count
# print('Average:', a)

# numList = list()
# while True:
#     inp = input('Please insert number:')
#     if inp == 'done': break
#     value = float(inp)
#     numList.append(value)
# a = sum(numList)/len(numList)
# print('Average:', a)

# fhand = input('please type filename:')
# inp = open(fhand)
# for data in inp:
#     data = data.rstrip()
#     if not data.startswith('From '): continue
#     data = data.split()
#     data = data[1]
#     data = data.split('@')
#     data = data[1]
#     print(data)


# # fname = input("Enter file name: ")
# fh = open('romeo.txt')
# lst = list()
# count = list()
# for line in fh:
#     line = line.split()
#     # print(repr(line))
#     count.append(line)
# count = count[0] + count[1] + count[2] + count[3]
# # print(count)
# for newList in count:
#     # print(repr(newList))
#     if newList not in lst:
#         lst.append(newList)
# lst.sort()
# print(lst)


# fh = open(fname)
# lst = list()
# count = list()
# for line in fh:
#     line = line.split()
#     for lin in line:
#         if lin not in lst:
#             lst.append(lin)
# lst.sort()
# print(lst)


# fname = input('Please insert file:')
# fh = open(fname)
# count = 0
# for hand in fh:
#     if not hand.startswith('From '):
#         continue
#     count = count + 1
#     hand = hand.split()
#     print(hand[1])
# print('There were ', count, 'lines in the file with From as the first word') 



# To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of unique words, which will contain the final result. Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.

# lst = list()
# fhand = open('romeo.txt')
# for hand in fhand:
#     hand = hand.split()
#     for hind in hand:
#         # print(hind)
#         if hind not in lst:
#             lst.append(hind)
# print(lst)



