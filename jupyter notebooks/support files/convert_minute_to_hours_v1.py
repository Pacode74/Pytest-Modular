# https://realpython.com/python-modulo-operator/


class Student:
    version = 1

    def __init__(self, name):
        self.name = name
        self.study_sessions = []

    def add_study_sessions(self, sessions):
        self.study_sessions += sessions


def total_study_time_in_hours(student, total_mins):
    hours = total_mins // 60
    minutes = total_mins % 60

    print(f"{student.name} studied {hours} hours and {minutes} minutes")


jane = Student("Jane")
jane.add_study_sessions([120, 30, 56, 260, 130, 25, 75])
total_mins = sum(jane.study_sessions)
total_study_time_in_hours(jane, total_mins)
