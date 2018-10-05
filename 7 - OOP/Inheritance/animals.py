class Animal:
    def __init__(self,n,ag,we):
        self.name = n
        self.__age = ag
        self.__weight = we

    # __str__ return readable str
    #__repr__ return  internal representation
    def __str__(self):
        return (f'\
                Name: {self.name} \n\
                Age: {self.__age} \n\
                Weight: {self.__weight}')