#Module7
#Excercise1
seasons=("winter","spring","summer","autumn")
month_num=int(input("Enter the month number from 1-12: "))
if month_num in[12,1,2]:
    season=seasons[0]
elif month_num in [3,4,5]:
    season=seasons[1]
elif month_num in [6,7,8]:
    season=seasons[2]
else:
    season=seasons[3]
print(f"The season for {month_num} is {season}.")
#Excercise2
names=set()
while True:
    name = input("Enter a name or press enter to quit: ")
    if name=="":
        break
    if name in names:
        print("Existing name.")
    else:
        print("New name.")
        names.add(name)
print("\nList of names: ")
for name in names:
    print(name)

#Excercise3
airport_data= {}
while True:
    print("\nChoose an option:")
    print("1: Enter a new airport")
    print("2: Fetch airport information")
    print("3: Quit")
    choice = input("Enter your choice (1/2/3): ")
    if choice=="1":
        icao_code= input("Enter icao code: ")
        airport_name=input("Enter airport name: ")
        if icao_code in airport_data:
            print(f"Airport with ICAO code {icao_code} already exists.")
        else:
            airport_data[icao_code] = airport_name
            print(f"Airport {airport_name} with ICAO code {icao_code} added.")
    elif choice=="2":
        icao_code= input("Enter icao code to fetch data: ")
        if icao_code in airport_data:
            print(f"The airport name for ICAO code {icao_code} is {airport_data[icao_code]}.")
        else:
            print(f"No airport found with ICAO code {icao_code}.")
    elif choice=="3":
        print ("End of Program")
        break
    else:
        print("Invalid choice. Please choose 1,2, or 3.")