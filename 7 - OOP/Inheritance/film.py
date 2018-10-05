class Film:
    def __init__(self,au,t):
        self.author = au
        self.type = t

    @property
    def __str__(self):
        return (f' Method in Film object: \n\
         Author: {self.author}\n\
         Type: {self.type}')
                