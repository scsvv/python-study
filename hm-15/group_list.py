class Student:

    def __init__(self, name: str, age: int, marks: list[int]):
        self.name = name
        self.age = age
        self.marks = marks


class Group:
    def __init__(self, students=None):
        if students is None:
            students = []
        self.students = students

    def add_to_group(self, student: Student) -> None:
        self.students.append(student)
        print(f'Student {student.name} added to AT183 GROUP')

    def remove_from_group(self, student: Student) -> None:
        self.students.remove(student)
        print(f'Student {student.name} removed from AT183 GROUP')

    def print_group_info(self, line_width: int = 30) -> None:
        for student in self.students:
            line = ""

            for i in range(len(student.marks)):
                line += str(student.marks[i])

                if i < len(student.marks) - 1:
                    line += " "
            print(student.name + line.rjust(
                line_width - len(student.name)))


if __name__ == "__main__":

    group = Group()
    student_1 = Student("Skorobohatov", 12, [10, 10, 2, 5])
    group.add_to_group(student_1)
    student_2 = Student("Volkov", 18, [11, 12, 12, 10])
    group.add_to_group(student_2)
    student_3 = Student("Skripkin", 19, [9, 8, 7, 9])
    group.add_to_group(student_3)

    group.print_group_info()
