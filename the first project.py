#this a combination of all the code in chapters 2 of 'Python Crash Course' by Eric Matthes and is a very basic and fun bit of code
message = ("Hello Python Projects world")
print (message) 
first_name = "chris"
last_name ="kim"
full_name = first_name + " " + last_name

message =  ("hello, " + full_name.title() + " We hope you have a great day at work this afternoon")
print (message) 
#note: that everything in python has to be exact so proof reading is key
name = input ("Please enter your name: " )
print ("hello " + name + " ! " )
age = input ("how old are you")
age = int(age)
if age >= 21:
    print ("\nWelcome most noble gentleman!")
else:
    print ("\nTry again when you've developed some good sense")
#see the above allows python to read numbers 
