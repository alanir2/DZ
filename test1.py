import unittest


class Student:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name
class TestStudent(unittest.TestCase):

    def test_walk_distance(self):
        student = Student("John")
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 50, "Дистанции не равны {student} != 500")

    def test_run_distance(self):
        student = Student("Alice")
        for _ in range(10):
            student.run()
        self.assertEqual(student.distance, 100, "Дистанции не равны {} != 100".format(student.distance))

    def test_running_vs_walking(self):
        running_student = Student("Bob")
        walking_student = Student("Eve")
        for _ in range(10):
            running_student.run()
            walking_student.walk()
        self.assertLess(running_student.distance, walking_student.distance,
                           "{} должен преодолеть дистанцию больше, чем {}".format(running_student.name,
                                                                                  walking_student.name))

if __name__ == '__main__':
    unittest.main()