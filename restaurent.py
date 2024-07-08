from menu import Menu
class restaurent:
    def __init__(self,name):
        self.name=name
        self.Employs=[]     #database of employees
        self.menu=Menu()
    def add_employee(self, employee) :
        self.Employs.append(employee)
    def view_employ(self):
        print('List of Employees')
        for emp in self.Employs:
            print(emp.name,emp.phone,emp.email,emp.adress,emp.age,emp.salary)