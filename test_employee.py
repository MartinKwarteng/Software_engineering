import unittest
from employee import Employee

# Class to inherit unittest 
class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp1 = Employee('Martin', 'Tee', 100)
        emp2 = Employee('Sir', 'Cool', 2000)

        self.assertEqual(emp1.email, 'Martin.Tee@gmail.com')
        self.assertEqual(emp2.email, 'Sir.Cool@gmail.com')

        emp1.first = 'Mathew' # various edge cases when the first name is changed 
        emp2.last = 'Sir' 

        self.assertEqual(emp1.email, 'Mathew.Tee@gmail.com')
        self.assertEqual(emp2.email, 'Sir.Sir@gmail.com')


    def test_fullname(self):
        emp1 = Employee('John', 'Ansah', 2000)
        emp2 = Employee('Zack', 'Moh', 5000)

        self.assertEqual(emp1.fullname, 'John Ansah')
        self.assertEqual(emp2.fullname, 'Zack Moh')

        emp1.first = 'Owusu'
        emp2.first = 'Dragon'

        self.assertEqual(emp1.fullname, 'Owusu Ansah')
        self.assertEqual(emp2.fullname, 'Dragon Moh')


    def test_apply_raise(self):
        emp1 = Employee('John', 'Ansah', 2000)
        emp2 = Employee('Zack', 'Moh', 5000)

        emp1.apply_raise()
        emp2.apply_raise()

        self.assertEqual(emp1.pay, 2100)
        self.assertEqual(emp2.pay, 5250)



if __name__ =='__main__':
    unittest.main()

