import mysql.connector
import geopy.distance

connection= mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user='user1',
    password= '12345',
    autocommit=True,
    collation = 'utf8mb4_unicode_ci'
   )
#Exercise1
def get_airport_by_icao(icao):
    sql= f"SELECT name, municipality FROM airport WHERE ident= '{icao}'"
    cursor=connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchone()
    return result

icao= input("Enter the ICAO code of airport: ")
print(f"The name of {icao} icao code is {get_airport_by_icao(icao)}.")

#Exercise2
def get_airport_by_country(country):
    sql= f"SELECT name, type FROM airport where iso_country='{country}'order by type"
    cursor=connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result)
    if cursor.rowcount>0:
        for row in result:
            print(f"{row[0]} is {row[1]}.")
country_code= input("Enter the country code: ")
get_airport_by_country(country_code)

#Exercise3
def get_airport_coordinates (icao):
    sql= f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '{icao}'"
    cursor=connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchone()
    return result

icao_code1= input("Enter ICAO code for airport 1: ")
coordinate_1 =get_airport_coordinates(icao_code1)
icao_code2= input("Enter ICAO code for airport 2: ")
coordinate_2= get_airport_coordinates(icao_code2)
print(f"The distance between the two airports is {geopy.distance.distance(coordinate_1, coordinate_2).km: .2f}km.")
