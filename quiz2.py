f = open('data.txt', 'r')
data_dict = {}
data = f.read()
open_program = True

class Employee:
    id : ""
    name : ""
    position : ""
    salary : 0

    def __init__(self, id: int, name: str, position: str, salary: int):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def getID(self) -> int:
        return self.__id

    def getName(self) -> str:
        return self.__name.title()

    def getPosition(self) -> str:
        return self.__position.title()

    def getSalary(self) -> int:
        return self.__salary


class Office():



while True:
    while open_program:

        print(data)
        print("1. New Staff")
        print("2. Delete Staff")
        print("3. View Summary Data")
        print("4. Save & Exit")
        user = input("Input Choice")
        if user == "New Staff":
            print("New Staff")
            new_id = input("Input ID[SXXXX]:")
            new_name = input("Input Name:")
            new_position = input("Input Position[Staff|Manager|Officer]:")
            new_salary = input("Input Salary:")
        if user == "Delete staff":
            print("Delete staff")
            del_staff = input("Input ID[SXXXX]:")
            print("Data has been successfully deleted")
        if user == "View Summary Data":
            print("View Summary Data")
            print("1. Staff")
            print("Minimum Salary:")
            print("Maximum Salary:")
            print("Average Salary:")
            print("2. Officer")
            print("Minimum Salary:")
            print("Maximum Salary:")
            print("Average Salary:")
            print("3. Manager")
            print("Minimum Salary:")
            print("Maximum Salary:")
            print("Average Salary:")
        if user == "Save & Exit":

            break



