import random
#Module5
#Excercise1
roll_dice= int(input("How many dice to roll? "))
sum= 0
for i in range(roll_dice):
    roll= random.randint(1,6)
    sum+=roll
print(f"The sum is {sum}.")

#Excercise2
user_input= input("Enter a number: ")
numbers=[]
while user_input!="":
    numbers.append(int(user_input))
    user_input= input("Enter a number: ")
numbers.sort(reverse=True)
print(numbers[0:5])

#Excercise3
num= int(input("Enter a number: "))
if num<2:
    print(f"{num} is not a prime number.")
else:
    for i in range(2,num):
        if num %i==0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")

#Excercise4
city_names=[]
for i in range(5):
    city_names.append(input("Enter a city name: "))
for city in city_names:
    print(city)