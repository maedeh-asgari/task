import unittest
from task import Person,Student,Teacher

class test_teacher(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.person=Person('Maedeh','Asgari')
        self.student=Student('Zahra','Ahamadi',19)
        self.teacher=Teacher('Ali','Miri')
    
    @classmethod
    def tearDownClass(self):
        del self.person
        del self.student
        del self.teacher

    def test_person_str(self):
        result=str(self.person)
        self.assertIn('Person',result)

    def test_student_str(self):
        result=str(self.student)
        self.assertIn('Student',result)

    def test_teacher_str(self):
        result=str(self.teacher)
        self.assertIn('Teacher',result)

if __name__=='__main__':
    unittest.main()
    
