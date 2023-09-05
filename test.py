import unittest
from task import Person, Student, Teacher


class TaskTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.person = Person('Maedeh', 'Asgari')
        cls.student = Student('Zahra', 'Ahmadi', 19)
        cls.teacher = Teacher('Ali', 'Miri', 2)
    
    @classmethod
    def tearDownClass(cls):
        del cls.person
        del cls.student
        del cls.teacher

    def test_person_str(self):
        result = str(self.person)
        print(result)
        self.assertEqual('Person: Maedeh Asgari', result)

    def test_student_str(self):
        result = str(self.student)
        print(result)
        self.assertEqual('Student: Zahra Ahmadi', result)

    def test_teacher_str(self):
        result = str(self.teacher)
        print(result)
        self.assertEqual('Teacher: Ali Miri', result)


if __name__ == '__main__':
    unittest.main()
