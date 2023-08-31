#parent
class Person():
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname

    def fullname(self):
        return self.name+' '+self.lastname
    

#child1
class Student(Person):
    def __init__(self,name,lastname,score):
        super().__init__(name,lastname)
        self.score=score
    
    def stufullname(self):
        return super().fullname()

#child2
class Teacher(Person):
    def __init__(self,name,lastname,stu_obj):
        super().__init__(name,lastname)
        self.stu_obj=stu_obj
    
    def tchfullname(self):
        return super().fullname()
    
    def __str__(self):
        return f'Student: {self.stu_obj.name} {self.stu_obj.lastname}'
    
#object 
stu1=Student('Zahra','Ahmadi',19)
tch1=Teacher('Ali','Akbari',stu1)

#call
print(stu1.stufullname())
print(tch1)

    
