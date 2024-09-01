#Module2
#Excercise1
name= input("Please tell me your name: ")
print(f"Hello, {name}!")

#Excercise2
radius= int(input("Radius of the circle: "))
square_of_radius= radius**radius
area= square_of_radius*22/7
print(f"The area of the circle is {area:.2f}")

#Excercise3
length= int(input("Length of the rectangle: "))
width= int(input("Width of the rectangle: "))
perimeter= (length+width)*2
area= length*width
print(f"The perimeter of rectangle is {perimeter} and the area is {area}. ")

#Excercise4
integer_1= int(input("Enter 1st integer number: "))
integer_2= int(input("Enter 2nd integer number: "))
integer_3= int(input("Enter 3rd integer number: "))
sum= integer_1 + integer_2 + integer_3
product= integer_1*integer_2*integer_3
average= sum/3
print(f"The sum is {sum}, the product is {product}, and the average is {average}.")

#Excercise5
talents= int(input("Enter talents: "))
pounds= int(input("Enter pounds: "))
lots= int(input("Enter lots: "))
grams= ((talents*20+pounds)*32+lots)*13.3
kilograms= grams/1000
print(f"The weight in kilograms is {kilograms:.2f} and in grams is {grams:.2f}.")

#Excercise6
import random
three_digit_code = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
print(f"The three digit lock number is {three_digit_code}")
four_digit_code = str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6))
print(f"The four digit lock number is {four_digit_code}")