#Module4
#Excercise1
num=1
while num<=1000:
    if num%3==0:
        print(num)
    num=num+1

#Excercise2
value_inches= float(input("Enter a value in inches: "))
while value_inches>0:
    value_cm= value_inches*2.54
    print(f"{value_inches} inches is equal to {value_cm} cm")
    value_inches= float(input("Enter a value in inches: "))
print("You entered a negative value. Goodbye.")

#Excercise3
smallest= 0
largest= 0
while True:
    user_input = input("Enter a number or press enter to quit: ")
    if user_input=="":
        break
    number=float(user_input)
    if number<smallest:
        smallest=number
    if number>largest:
        largest=number
if user_input!="":
    print(f"Smallest number is {smallest} and largest number is {largest}")

#Excercise4
import random
num= random.randint(1,100)
guess=0
while not guess==num:
    guess= int(input("Enter your guess! "))
    if guess> num:
        print("Your guess is too high")
    elif guess< num:
        print("Your guess is too low")
    else:
        print("Your guess is correct")

#Excercise5
username= "python"
password= "rules"
num_try=5
while num_try>0:
    name=input("Enter your username: ")
    pas=input("Enter your password: ")
    if name==username and pas==password:
        print("Welcome dear user!")
        break
    num_try=num_try-1
else:
    print("Acess denied. You have used all the 5 tries.")

#Excercise 6
import random
import math
random_points= int(input("How many random points do you want? "))
inside_points=0
i=0
while i<random_points:
    x= random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2 + y**2<1:
        inside_points= inside_points+ 1
    i=i+1
pi= 4*inside_points/random_points
print(f"The pi estimation is {pi}, the difference with math pi is {math.pi-pi}.")