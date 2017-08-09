from unittest import TestCase
from py_2017_1 import MyClass

class TestMyClass(TestCase):
    def test_func1(self):
        s=MyClass()
        self.assertRaises(Exception,s.myclass_func1)
    def test_myclass_func1(self):
        self.fail()
