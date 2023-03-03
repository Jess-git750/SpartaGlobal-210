print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
print(x[0:5])
#or
#for i in range(5):
#    print(x[i])

# A1a:

'''

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
a = []
for number in x:
    if number % 2 == 0:
        a.append(number)
print(a)

# A1b:



#print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
for i in range(5):
    if x[i] %2 == 0 :
        print(x[i])

x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
a = []
for number in range [0:5]:
    if number % 2 == 0:
        a.append(number)
print(a)
# A1c:


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
y=[]
for x in range(len(names)):
    y.append(names[x][0])
print(y)
#for name in names:
    l.appemd(name.index)

# A2a:




print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
y=[]
for x in range(len(names)):
    y.append(names[x].index(" "))
print(y)
# A2b:




print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]


initials = []

for name in names:

    firstname = name.split(" ")[0]
    lastname = name.split(" ")[1]
    initials.append(firstname[0] + lastname[0])

print(initials)


# A2c:


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


for i in list_of_lists :
    if len(set(i)) == len(i):
        print(i)
'''

# A3a:


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:


while True:
    number = int(input("Give me a number greater than 100: "))
    if number > 100:
        print("Congrat")
        break
    else:
        print("Try again")

    print(number)



print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return print("Not prime")
  return print("prime")

while True:
    number = int(input("Give me a number greater than 100: "))
    if number > 100:
        print("Congrat")
        is_prime(number)
        break
    else:
        print("Try again"),
        is_prime(number)
    print(number)



'''
while True:
    number = int(input("Give me a number greater than 100: "))
    if number > 100:
        print("Congrat")

        if number > 1:
             for i in range(2, int(number/2)+1):
                 if (number % i) == 0:
                     print("This is not a prime number")
        else:
            print("This is a prime number")

        break

    else:
        print("Try again")
        if number > 1:
            for i in range(2, int(number / 2) + 1):
                if (number % i) == 0:
                    print("This is not a prime number")
                else:
                    print("This is a prime number")
            
'''

