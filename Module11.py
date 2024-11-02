#Module11
#Exercise1
class Publication:
    def __init__(self,name):
        self.name=name
    def print_info(self):
        print(self.name,end=" ")
class Book(Publication):
    def __init__(self,name, author, pages):
        super().__init__(name)
        self.author=author
        self.pages=pages
    def print_info(self):
        super().print_info()
        print(f"Author: {self.author}, Pages: str{self.pages}")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor=editor

    def print_info(self):
        super().print_info()
        print(f"Editor: {self.editor}")

pub=[]
pub.append(Magazine("Donald Duck","Aki Hyppa"))
pub.append(Book("Compartment No. 6", "Rosa Likson", 192))
for i in pub:
    i.print_info()

#Exercise2
class Car:
    def __init__(self, registration_num, max_speed):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self,change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def drive(self,hours):
        distance= self.current_speed*hours
        self.travelled_distance+=distance
class ElectricCar(Car):
    def __init__(self,registration_num, max_speed, battery_capacity):
        super().__init__(registration_num, max_speed)
        self.battery_capacity=battery_capacity
    def print_distance(self):
        print(f"Distance: {self.travelled_distance}")

class GasolineCar(Car):
    def __init__(self, registration_num, max_speed, tank_capacity):
        super().__init__(registration_num, max_speed)
        self.tank_capacity = tank_capacity

    def print_distance(self):
        print(f"Distance: {self.travelled_distance}")

el_car1= ElectricCar("ABC-15", 180, 52.5)
gas_car1= GasolineCar("ACD-123", 165, 32.3)
el_car1.accelerate(30)
gas_car1.accelerate(100)
el_car1.drive(3)
gas_car1.drive(3)
el_car1.print_distance()
gas_car1.print_distance()