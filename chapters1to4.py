import math, random

'''hours_prompt = "How many hours did you work? "
rate_prompt = "What is your hourly rate? "
hours = input(hours_prompt)
rate = input(rate_prompt)
pay = int(hours) * int(rate)
print("You earned $" + str(pay) + ".")'''

'''x = 3
if x > 1:
    print("x is greater than 1")

# pass for now, with edit in the future
if x < 2:
    pass
else:
    print ('x is greater than 2')'''

'''x = 2
y = 2

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')'''

'''x = -9999
y = 1000

if x < y:
    print('x is less than y')
else:
    if x > y:
        print('x is greater than y')
    else:
        print('x and y are equal')'''

'''inp = input('Enter temperature in F: ')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0/9.0
    print('Temperature in C is ' + str(cel))
except:
    print("Please enter a valid (numeric) temperature!")'''

'''inp1 = input("How many hours did you work: ")
inp2 = input("What was your rate: ")

try:
    hrs = int(inp1)
    rate = int(inp2)

    if hrs <= 40:
        pay = hrs * rate
        print(str(pay))
    else:
        pay = (40*rate) + (hrs - 40)*(rate*1.5)
        print(str(pay))
except:
    print("Please enter a number for both rate and hours.")'''

'''print(math)
print('hello world')
print('git test')

decibels = 10*math.log10(4)
print(decibels)

degrees = 45
radians = degrees / 360 * 2 * math.pi
print(radians)'''

'''for i in range(10):
    x = random.random()
    print(x)'''

'''y = random.randint(5,10)
print(y)'''

#defining functions
'''def print_lyrics():
    print("test lyrics")
    print("test line 2")

#print_lyrics()

#function in a function
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()'''

# functions with arguments
'''def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice("Cat")
print_twice(4)
print_twice(math.pi)
print_twice('Spam '*4)
print_twice('Span Spam Spam Spam')'''

# using Return with void functions
def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3,4)
print(x)
