def print_lyrics():                               #this is a basic function, since it
    print("I'm a lumberjack, and I'm ok." )       #has nothing in the parenthesis it 
    print("I sleep all night and work all day.")  #takes no arguments

print_lyrics

print_lyrics()

def print_twice(string):   #this is a function that takes a string as an
    print(string)          #argument and prints it twice
    print(string)

print_twice("Dennis Moore, ")

def repeat(word, n):
    print(word * n)

spam = 'Spam, '
repeat(spam, 4)

def first_two_lines():
    repeat(spam, 4)
    repeat(spam, 4)

first_two_lines()

def last_three_lines():
    repeat(spam, 2)
    print('(Lovely Spam, Wonderful Spam!)')
    repeat(spam, 2)

last_three_lines()

def print_verse():
    first_two_lines()
    last_three_lines()

print_verse()

for i in range(2):
    print("Verse", i)
    print_verse()
    print()

def print_n_verses(n):
    for i in range(n):
        print_verse()
        print()

print_n_verses(4)