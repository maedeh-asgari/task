# parent
class Person:
    prefix = 'per'

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    @property
    def full_name(self):
        return self.name + ' ' + self.lastname
    
    def __str__(self):
        return f'{type(self).__name__} : {self.name} {self.lastname}'
    
    def get_full_name_with_prefix(self):
        return f'{self.prefix}: {self.name} {self.lastname}'


# child1
class Student(Person):
    prefix = 'stu'

    def __init__(self, name, lastname, score):
        super().__init__(name, lastname)
        self.score = score


# child2
class Teacher(Person):
    prefix = 'tch'

    def __init__(self, name, lastname, level):
        super().__init__(name,  lastname)
        self.level = level


# new class
class Maker:
    def __init__(self, prefix, *args, **kwargs):
        self.prefix = prefix
        self.args = args
        self.kwargs = kwargs

    def create_instance(self):
        if self.prefix == 'per':
            return Person(*self.args, **self.kwargs)
        elif self.prefix == 'stu':
            return Student(*self.args, **self.kwargs)
        elif self.prefix == 'tch':
            return Teacher(*self.args, **self.kwargs)


s = Maker(prefix='stu', name='Maedeh', lastname='Asgari', score=20)
t = Maker(prefix='tch', name='Maral', lastname='Asadi', level=1)

print(s.create_instance())
print(t.create_instance())
