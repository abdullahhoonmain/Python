class Car:
    def __init__(self,color,name,year):
        self.__color = color
        self.__name = name
        self.__year = 0000

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def driving(self):
        print(f"{self.__name} is driving")

    def stopped(self):
        print(f"{self.__name} has stopped")

    def display(self):
        print(f"Name: {self.__name}, Color: {self.__color}, Year: {self.__year}")


car = Car("toyota", "black", 2024)
car.set_name("BMW")
car.display()  # Output: Name: BMW, Color: black, Year: 2024
