# https://realpython.com/python-modulo-operator/


class Student:
    def __init__(self, name):
        self.name = name
        self.study_sessions = []

    def add_study_sessions(self, sessions):
        self.study_sessions += sessions

    def __mod__(self, other):
        return sum(self.study_sessions) % other

    def __floordiv__(self, other):
        return sum(self.study_sessions) // other


def total_study_time_in_hours(student):
    hours = student // 60
    minutes = student % 60

    print(f"{student.name} studied {hours} hours and {minutes} minutes")


jane = Student("Jane")
jane.add_study_sessions([120, 30, 56, 260, 130, 25, 75])
total_study_time_in_hours(jane)

# By overriding .__mod__(), you allow your custom classes to behave more like
# Python’s built-in numeric types.
