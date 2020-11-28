#importing the library
import random #to randomy generate a number 

def func():                     #to print and generate a random number 
    n = random.randint(1,6)     #Generating a random number between 1 and 6
    return n                    #returning the random number 


user_input1 = input("\nWould you like to roll the dice(y/n) : ") #input from user to roll the dice
f = func()                                                       #calling the function    
print(f)                                                         #printing the random number 
while user_input1 == 'y':                                        #while loop is use to ask the user to play again
    user_input = input("\nWould you like to roll the dice again(y/n): ")
    if user_input == 'y':
        f1 = func()
        print(f1)
        continue                                                 #to continue asking user whether to roll the again or not
    else:                                                        #if the answer is no then the program will just stop
        print("\nExiting!!!!!!")
        exit()                                                   #To terminate the execution