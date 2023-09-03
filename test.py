import unittest
from task import Person,Student,Teacher

class test_teacher(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.person=Person('Maedeh','Asgari')
        self.student=Student('Zahra','Ahmadi',19)
        self.teacher=Teacher('Ali','Miri')
    
    @classmethod
    def tearDownClass(self):
        del self.person
        del self.student
        del self.teacher

    def test_person_str(self):
        result=str(self.person)
        self.assertEqual('Person: Maedeh Asgari',result)

    def test_student_str(self):
        result=str(self.student)
        self.assertEqual('Student: Zahra Ahmadi',result)

    def test_teacher_str(self):
        result=str(self.teacher)
        self.assertEqual('Teacher: Ali Miri',result)

if __name__=='__main__':
    unittest.main()
