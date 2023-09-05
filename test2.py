import unittest
from task import Person, Student, Teacher, Maker


class TestMaker(unittest.TestCase):

    def test_create_instance_person(self):
        maker = Maker(prefix='per', name='Maedeh', lastname='Asgari')
        instance = maker.create_instance()
        self.assertIsInstance(instance, Person)
        self.assertEqual(instance.name, 'Maedeh')
        self.assertEqual(instance.lastname, 'Asgari')

    def test_create_instance_student(self):
        maker = Maker(prefix='stu', name='Zahra', lastname='Ahmadi', score=20)
        instance = maker.create_instance()
        self.assertIsInstance(instance, Student)
        self.assertEqual(instance.name, 'Zahra')
        self.assertEqual(instance.lastname, 'Ahmadi')
        self.assertEqual(instance.score, 20)

    def test_create_instance_teacher(self):
        maker = Maker(prefix='tch', name='Sara', lastname='Miri', level=1)
        instance = maker.create_instance()
        self.assertIsInstance(instance, Teacher)
        self.assertEqual(instance.name, 'Sara')
        self.assertEqual(instance.lastname, 'Miri')
        self.assertEqual(instance.level, 1)


if __name__ == '__main__':
    unittest.main()