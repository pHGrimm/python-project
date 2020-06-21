# This program says hello and asks for my name

print('HELLO, YOU!')
print('WHO ARE YOU?')  # ask for a name
myName = input()
print('It is great to learn what your name is,' + myName)
print('The length of your name is:')
print(len(myName))
print('How old you is?') # ask for age
myAge = input()
print('You will be' + str(int(myAge) + 1) + 'in one yearlings.')
