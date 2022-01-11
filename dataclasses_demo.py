from dataclasses import dataclass
from typing import List

class Student:
    # No logical equality, no logical comparison, no easy way to freeze, bad repr, too verbose
    def __init__(self, student_id, age, courses):
        self.student_id = student_id
        self.age = age
        self.courses = courses

print(Student(100, 18, ["CS 1310", "CS 1333", "MATH 1552"]))
print(Student(200, 21, ["PHIL 1310", "CS 1333"]))

# Talk about equality, ordering and frozen
@dataclass()
class StudentDataClass:
    student_id: int
    age: int
    courses: List[int]

student_data_1 = StudentDataClass(100, 18, ["CS 1310", "CS 1333", "MATH 1552"])
student_data_2 = StudentDataClass(200, 21, ["PHIL 1310", "CS 1333"])
student_data_2.student_id = 500
