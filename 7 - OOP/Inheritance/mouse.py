from MultipleInheritance.animals import *
from MultipleInheritance.film import *

class Mouse(Animal,Film):
    def __init__(self,name, age, weight, author,type):
        Animal.__init__(self, name, age, weight)
        Film.__init__(self, author, type)

m = m = Mouse('Mickey', 3, 11, 'Walt Disneey', 'Cartoon')
print(m.__str__())


