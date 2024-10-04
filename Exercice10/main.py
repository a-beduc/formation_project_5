class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"The person name is {self.name}")
        print(f"The person age is {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"The employee salary is {self.salary}")


def main():
    jack = Person("Jack", 25)
    bobby = Employee("Bobby", 30, 5000)
    print('---- Test Person ----')
    jack.display_details()
    print('\n---- Test Employee ----')
    bobby.display_details()


if __name__ == "__main__":
    main()