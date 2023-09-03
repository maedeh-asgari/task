#parent
class Person():
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
        self.full_name
    @property
    def full_name(self):
        return self.name+' '+self.lastname
    
    def __str__(self):
        return type(self).__name__+f': {self.name} {self.lastname}'
    
    def get_full_name_with_prefix(self):
        if type(self).__name__=='Person':
            return f'per: {self.name} {self.lastname}'
        if type(self).__name__=='Student':
            return f'stu: {self.name} {self.lastname}'
        if type(self).__name__=='Teacher':
            return f'tch: {self.name} {self.lastname}'

    
#child1
class Student(Person):
    def __init__(self,name,lastname,score):
        super().__init__(name,lastname)
        self.score=score
    
#child2
class Teacher(Person):
    def __init__(self,name,lastname):
        super().__init__(name,lastname)
