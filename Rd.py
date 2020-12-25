import random  # Importing random module
import time  # Importing time module

repeat = 1 # repeat Variable
sleeptime = 1 # Variable of time of sleeping in seconds
word = input("Start? ")  # Quest user for start of the program
sv = 0 # some Variable

if word == "yes":  # Check for answer yes

    print("Generating",end = "") # Printing Generating in the console without a new line

    time.sleep(sleeptime) # Waiting sleepime seconds betwen actions

    print(".",end = "") # Printing . in the console without a new line

    time.sleep(sleeptime) # Waiting sleepime seconds betwen actions

    print(".",end = "") # Printing . in the console without a new line

    time.sleep(sleeptime) # Waiting sleepime seconds betwen actions

    print(".") # Printing . in the console with a new line

    time.sleep(sleeptime) # Waiting sleepime seconds betwen actions
        
    print("Done!") # Showing Done! in the console

    time.sleep(slleptime) # Waiting sleepime seconds betwen actions

else: # If user type something else
        
    print("Generating",end = "") # Printing Generating in the console without a new line

    time.sleep(sleeptime) # Waiting sleepime seconds betwen actions

    print(".",end = "") # Printing . in the console without a new line

    time.sleep(sleeptime) # Waiting sleepime seconds betwen actions

    print(".",end = "") # Printing . in the console without a new line

    time.sleep(sleeptime) # Waiting sleepime seconds betwen actions

    print(".") # Printing . in the console with a new line

    time.sleep(sleeptime) # Waiting sleepime seconds betwen actions
        
    print("Done!") # Showing Done! in the console

    time.sleep(sleeptime) # Waiting sleepime seconds betwen actions
        
        

number = random.random() # Genrating number between 0 and 1

number = number // 0.01 # converting this number up to hundred



print("Your number is",int(number)) # Showing this number in the console, and convert it to int

time.sleep(sleeptime)

while repeat == 1:
    try:
        num = int(input("Want to repeat? 1 - yes. 2 - stop the porgramm "))
        if num == 1:
            print("Generating",end = "") # Printing Generating in the console without a new line

            time.sleep(sleeptime) # Waiting sleepime seconds betwen actions

            print(".",end = "") # Printing . in the console without a new line

            time.sleep(sleeptime) # Waiting sleepime seconds betwen actions

            print(".",end = "") # Printing . in the console without a new line

            time.sleep(sleeptime) # Waiting sleepime seconds betwen actions

            print(".") # Printing . in the console with a new line
    
            time.sleep(sleeptime) # Waiting sleepime seconds betwen actions
        
            print("Done!") # Showing Done! in the console

            time.sleep(sleeptime) # Waiting sleepime seconds betwen actions
    
            number = random.random() # Genrating number between 0 and 1

            number = number // 0.01 # converting this number up to hundred

            print("Your number is",int(number))
        
        elif num == 2:
            repeat = 0
        else:
            print("Some wrong!")
    except:
        print("You type something wrong!")

print("Work done!")
