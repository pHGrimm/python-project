# This program does something remedial TBD

print('Hello rookie')
print('Whats yer name?')  #ask for their name
myName = input()   #the input() function call is an expression that evaluates to whatever string the user typed in
print('What kind of name is that anyway... ' + myName)
print('Its ' + str(len(myName)) + ' whole characters long!')
    #You can pass the len() function a string value (or a variable containing a string),
    #and the function evaluates to the integer value of the number of characters in that string
print('What is your age?')    #ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in one year.')

#The str() function can be passed an integer value and will evaluate to
#a string value version of it

#The str(), int(), and float() functions will evaluate to the string,
#integer, and floating-point forms of the value you pass, respectively.

