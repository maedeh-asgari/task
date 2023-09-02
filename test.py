import unittest
from task import student,teacher,tch1

class test_teacher(unittest.TestCase):
    def test_str(self):
        result=str(tch1)
        self.assertIn('Student',result)

    