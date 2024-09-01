#Module3
#Excercise1

zander_cm_length= float(input("Enter the zander length in centimeters: "))
if zander_cm_length<42:
    difference_from_size_limit= 42-zander_cm_length
    print(f"Release the fish back to the lake because it is {difference_from_size_limit} cm below from the size limit.")
else:
    print("You can take the fish!")

#Excercise2
cabin_class= (input("Enter the cabin class: "))
if cabin_class=="LUX":
   print("Upper-deck cabin with a balcony.")
elif cabin_class=="A":
   print("Above the car deck, equipped with a window")
elif cabin_class=="B":
   print("Windowless cabin above the car deck")
elif cabin_class=="C":
  print("Windowless cabin below the car deck")
else:
   print("Invalid cabin class")

#Excercise3
biological_gender= input("Biological gender: ")
hemoglobin_value= int(input("Hemoglobin value in g/l: "))
if biological_gender=="female":
    if hemoglobin_value<117:
        print("Low hemoglobin")
    elif 117<=hemoglobin_value<=155:
        print("Normal hemoglobin")
    else:
        print("High hemoglobin")
if biological_gender=="male":
    if hemoglobin_value<134:
        print("Low hemoglobin")
    if 134<=hemoglobin_value<=167:
        print("Normal hemoglobin")
    if hemoglobin_value>167:
        print("High hemoglobin")

#Excercise4
year= int(input("Enter the year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
