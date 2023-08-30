#parent
class Person():
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname

    def fullname(self):
        return self.name+' '+self.lastname
    

#child
class Student(Person):
    def __init__(self,name,lastname,score):
        super().__init__(name,lastname)
        self.score=score
    
    def stufullname(self):
        return super().fullname()
    
#object 
stu1=Student('Zahra','Ahmadi',19)

#call
print(stu1.stufullname())

    