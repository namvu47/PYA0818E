# Attribute: properties of object
# Method: what object can do
# Ex: Object person has attribute (name, age, add, email) and method (run, walk, drink, eat)

#Ex:
class person:
    def __init__(self, name, age, add):
        self.full_name = name
        self.age = age
        self.address = add
        print("Full name: ", self.full_name)
        print('Age: ', self.age)
        print('Add: ', self.address)

instance_demo = person('Le Van A', 19, 'Ha Noi')
print(type(instance_demo))
print(instance_demo)

class employee():
    count = 0

    # 2 attributes: name, salary
    # tham so mac dinh 'salary' phai dat sau tham so bat buoc 'name'
    def __init__(self, name, salary=1000):
        self.name = name
        # __salary: private attr
        self.salary = salary
        employee.count += 1

    #method 1:
    # __numberEmployees: private method
    def numberEmployees(self):
        print ('So luong nhan vien: ', employee.count)

    #method 2:
    def showInfo(self):
        print('Name: ', self.name)
        print('Luong: ', self.salary)


# Khoi tao object -> instance
employee1 = employee('Nguyen Van A', 2000)
employee1.numberEmployees()
employee1.showInfo()
employee2 = employee('Nguyen Van B')
employee2.numberEmployees()
employee2.showInfo()

