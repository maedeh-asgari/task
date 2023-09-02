#parent
class person():
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname

    def full_name(self):
        return self.name+' '+self.lastname
    def get_type(self):
        return type(self).__name__
    

#child1
class student(person):
    def __init__(self,name,lastname,score):
        super().__init__(name,lastname)
        self.score=score
    
    def full_name(self):
        return super().full_name()

#child2
class teacher(person):
    def __init__(self,name,lastname,stu_obj):
        super().__init__(name,lastname)
        self.stu_obj=stu_obj
    
    def full_name(self):
        return super().full_name()
    
    def __str__(self):
        return f'Student: {self.stu_obj.name} {self.stu_obj.lastname}'
    
#object 
stu1=student('Zahra','Ahmadi',19)
tch1=teacher('Ali','Akbari',stu1)

#call
print(stu1.full_name())
print(tch1)
print(stu1.get_type())
print(tch1.get_type())
