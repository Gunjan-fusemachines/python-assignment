# University and Department classes with encapsulation and polymorphism in Python
class University:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__departments = []

    def add_department(self, department):
        self.__departments.append(department)

    def display_details(self):
        print(f"University Name: {self.__name}")
        print(f"Location: {self.__location}")
        print("Departments:")
        for department in self.__departments:
            department.display_details()

class Department(University):
    def __init__(self, name, head):
        super().__init__("", "")  # Empty name and location for Department
        self.__name = name
        self.__head = head
        self.__courses = []

    def add_course(self, course):
        self.__courses.append(course)

    def display_details(self):
        print(f"Department Name: {self.__name}")
        print(f"Head of Department: {self.__head}")
        print("Courses Offered:")
        for course in self.__courses:
            print(f"  - {course}")


# Create University and Department objects
university1 = University("ABC University", "New York")
university2 = University("XYZ University", "Los Angeles")

department1 = Department("Computer Science", "Prof. Smith")
department2 = Department("Physics", "Prof. Johnson")

# Add departments to universities
university1.add_department(department1)
university2.add_department(department2)

# Add courses to departments
department1.add_course("Intro to Programming")
department1.add_course("Data Structures")
department2.add_course("Mechanics")
department2.add_course("Thermodynamics")

# Display university and department details
university1.display_details()
print()
university2.display_details()
