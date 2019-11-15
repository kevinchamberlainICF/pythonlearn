#Chapter 6
print("chapter 6")

fruit = 'banana'
'''print(fruit[0])

length = (len(fruit))
print(length)

#get the last letter
last = fruit[length - 1]
print(last)
#OR
print(fruit[-1])'''

#traversing through a string
'''index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1'''

#traverse backwards
'''index = len(fruit)
while index > 0:
    letter = fruit[index - 1]
    print(letter)
    index = index - 1'''

'''for char in fruit:
    print(char)

print(fruit[1:4])
print(fruit[1:])
print(type(fruit[:]))

fruit = 'apple'
print(fruit)'''

# function for counting the letter A
'''def a_counter(word):
    counter = 0
    for char in word:
        if char == 'a':
            counter = counter + 1
    return(counter)

print(a_counter('abracadabra'))'''

'a' in 'banana'
