import Car
class Person:
    def __init__(self, name, age, occupation, netWorth):
        self.name = name
        self.age = age
        self.occupation = occupation
        self._netWorth = netWorth
    def get_netWorth(self):
        return self._netWorth
    def set_netWorth(self, netWorth):
        self._netWorth= netWorth
    def Info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Net Worth: Rs {self.get_netWorth()}")
        print(f"Occupation: {self.occupation}")

# Creating an instance of the Person class
a = Person("Abdullah", 20, "Student", 500)
a.Info()


class Employee(Person):
    def __init__(self, id,post, name, age,occupation, netWorth):
        super().__init__(name, age, occupation, netWorth)
        self.__ID= id
        self._post= post

    def Info(self):
        print(f"Emp name: {self.name}")
        print(f"Emp age: {self.age}")
        print(f"Emp occupation: {self.occupation}")
        print(f"Emp netWorth: {self._netWorth}")
        print(f"Emp id: {self.__ID}")
        print(f"Emp post: {self._post}")


    def getID(self):
        return self.__ID

    def setID(self, id):
        self.__ID= id

    def setPost(self, post):
        self._post= post

    def getPost(self):
        return self._post


b = Employee(7, "student", "Abdullah", 20, "Student", 500)
b.Info()