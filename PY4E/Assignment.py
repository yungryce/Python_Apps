"""
age = '2'
age = float(age)
yy = age + 2
print(yy)
bb = str(yy)
print(type(bb), bb)
# int, float, str
"""



"""
ab = input()
print(type(ab), ab) 
cd = int(ab) + 1
print(type(cd), cd)
"""


#print(int(98.9))

#x = 4
"""
if (x > 5):
    print("x is above 5")
if (x < 5):
    print("above ke")
"""

"""
#TRY & EXCCEPT
age = input('Please input a number:')
try:
	floatAge = float(age)
	print('Floatage:', floatAge)
except:
	strAge = str(age)
	print('StringAge:', strAge)

"""





"""
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
standardHours = 40
extraHours = h - standardHours
standardGross = standardHours * r
if (h <= 40):
    grossPay = r * h
    print(grossPay)
elif (h > 40):
    grossPay = (r * 1.5 * extraHours) + standardGross
    print(grossPay)
"""


"""
hrs = input("Enter Hours:")
rate = input("Enter Rate per Hour:")

def computepay(h, r):
    if (h <= standardHours):
        grossPay = standardPay
    elif (h > standardHours):
        grossPay = (1.5 * r * extraHours) + standardPay
    return grossPay

hrs = input("Enter Hours:")
rate = input("Enter Rate per Hour:")
h = float(hrs)
r = float(rate)

standardPay = r * h
standardHours = 40
extraHours = h - standardHours
    
p = computepay(10, 20)
print("Pay", p)
"""


"""
while True:
    line = input(":::::")
    if (line[0] == "#"):
        continue
    if line ==("Done"):
        break
print(line)
"""

"""
storage = -99
friends = ['tobi', 'afo', 'james', 'john', 'luigi']
for friend in friends:
    storage = friend
    print(friend, storage)
"""


"""
found = 0
count = 0
numbers = [1, 4, 8, 2, 9, 5, 8, 4, 2, 7, 2, 3, 7]
for number in numbers:
    number = found
    count = count + 1
    if (number == count):
        print(number)

"""


"""
largest = None
smallest = None
while True:
    nums = input("Please Insert Number: or done")
    
    if (nums == "done"):
        break
    else:
        try:
            num = int(nums)
        except:
            print("please retry")
    
    
    if (smallest is None):
        smallest = num
    elif (num < smallest):
        smallest = num
    if (largest is None):
        largest = num
    elif (num > largest):
        largest = num
print("Maximum:", largest, "Minimum:", smallest)
"""


"""
baby = "banana"
i = 0
while (i < len(baby)):
    print(i, baby[i])
    i = i + 1

for a in baby:
    print(a)
"""

"""
greet = "hello thoery"
print(type(greet))
great = greet.upper()
grret = greet.find("b")
grreet = greet.find("o")
print(great, grret, grreet)
#print(dir(great))
"""

"""
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
john = data.find("@")
juls = data.find(" ", john)
jude = data[john : 32]
print(john)
print(juls)
print(jude)
"""

text = "X-DSPAM-Confidence:    0.8475"
tect = text.find("0")
# toto = text.find("")
print(tect)
team = text[23:]
print(team)

fhand = open('trial.py','r')
count = 0
for eachLine in fhand:
    count = count + 1
    print(count, eachLine)