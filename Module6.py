import random
import math
#Module6
#Excercise1
def dice_roll():
    return random.randint(1, 6)
while True:
    dice=dice_roll()
    print(f"Dice shows {dice}.")
    if dice == 6:
        break

#Excercise2
def dice_roll_side (num):
    return random.randint(1, num)
num=int(input("How many sides in your dice? "))
while True:
    dice_side=dice_roll_side(num)
    print(f"Dice shows {dice_side}.")
    if dice_side == num:
        break

#Excercise3
def gallons_to_litres(gallons):
    return gallons * 3.78541
while True:
    user_input=int(input("How many gallons do you want to convert? "))
    if user_input<0:
        break
    print(f"{user_input} gallons is equal to {gallons_to_litres(user_input):.2f}. ")
"""
#Excercise4
    for number in range(10):
        ex_list.append(random.randint(1,10))
        print(f"The list of numbers is: ")
        for i in range(len(ex_list)):
            print(f"{ex_list[i]} ", end="")
        print(f"\n The sum of all the numbers is: {sum(ex_list)}. ")
"""
#Excercise5
def make_even(num_list):
    result=[]
    for i in range(len(num_list)):
        if num_list[i]%2==0:
            result.append(num_list[i])
        return result
def print_list(message, num_list):
    for i in range(len(num_list)):
        print(f"{num_list[i]} ", end="")
ex_list=[]
for n in range(10):
    ex_list.append(random.randint(1,99))
print_list("Original list", ex_list)
new_list= make_even(ex_list)
print_list("Only even number list", new_list)

#Excercise6
def pizza_quality(diameter,price):
    return price/math.pi*(diameter/200)**2
pizza1_diameter= float(input("Enter the diameter of the pizza 1 (in cm): "))
pizza1_price= float(input("Enter the price of the pizza 1 (in euros): "))
pizza2_diameter= float(input("Enter the diameter of the pizza 2 (in cm): "))
pizza2_price= float(input("Enter the price of the pizza 2 (in euros): "))
if pizza_quality(pizza1_diameter,pizza1_price)>pizza_quality(pizza2_diameter,pizza2_price):
    print("Go for Pizza 2!")
else:
    print("Go for Pizza 1!")