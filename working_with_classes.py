class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displaycount(self):
        print("Total Employee %d" % Employee.empCount)  # %s is used as a placeholder for string values you want to inject into a formatted string.
                                                        # %d is used as a placeholder for numeric or decimal values.

    def displayemployee(self):
        print("Name ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Greg", 1200)
emp2 = Employee("Frank", 2600)
emp1.displayemployee()
print("Total Employes %d" % Employee.empCount)