# fInput = input('Enter File Name:')
# count = 0
# try:
#     fHand = open(fInput, 'r')
# except:
#     print('File cannot be opened:', fInput)
#     exit()

# for eachLine in (fHand):
#     count = count + 1
#     # print(count)
#     # print(len(eachLine)) #one line seperated by /n to form multiple lines
#     eachLine = eachLine.rstrip()
#     #unintersting 
#     if not eachLine.startswith('From:'):
#         continue
#     # interesting
#     if (eachLine.find('@uct.ac.za') == -1):
#         continue
#     print(eachLine)
# print('There were', count, 'mail lines in', fInput)


# oyaRead = fHand.read()
# # print(len(oyaRead)) one line with all xters in a string
# ben = oyaRead[:1000]
# # print(oyaRead)

line = 'this is how we do it \n'
fOut = open('aboy.txt', 'w')
fOut.write(line)
line2 = 'labors of our \t heroes past \n'
fOut.write(line2)
fOut.close()
print(repr(line2))