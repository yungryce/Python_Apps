# inputData = input('please input file name:')
# fileName = open(inputData, 'r')
# for files in fileName:
#     upperFiles = files.upper()
#     if upperFiles.find('DSPAM-CONFIDENCE') == -1:
#         continue
#     upperFiles = upperFiles.rstrip()
#     print(upperFiles)
#     letsSee = upperFiles[:10]
#     print(letsSee)
#     # john = upperFiles.read()
#     # print(john[:100])


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0
fh = open(fname)
for line in fh:
    #line = line.read('X-DSPAM-Confidence:    0.8475')
    if not line.startswith("X-DSPAM-Confidence: "):
        continue
    count = count + 1
    # line = line.rstrip()
    line = line[20:]
    line = float(line)
    total = total + line
print(total/count)
