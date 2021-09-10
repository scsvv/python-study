def create_student(firstname: str, lastname: str, marks: float) -> dict:

    return {
        'firstname': firstname,
        'lastname': lastname,
        'marks': marks
    }


def calculate_average_grade(marks: list[int]) -> float:

    return sum(marks) / len(marks)


def format_info(student: dict, desired_width: int) -> str:

    fullname = "{} {}.".format(student['lastname'], student['firstname'][0])
    formatted_grade = "{:.2f}".format(student['marks'])
    return fullname + formatted_grade.rjust(desired_width-len(fullname))


def print_weak_students_and_score(students: list) -> None:

    for student in students:
        if student['marks'] < 5:
            print(format_info(student, 24))

    average_grades = [student['marks'] for student in students]
    print("Средний балл по классу: {:.2f}".format(
        calculate_average_grade(average_grades))
    )


def read_students_from(file) -> list:

    students = list()
    while True:
        line: str = file.readline()
        if not line:
            break

        firstname, lastname, *grades = line.split()
        marks = calculate_average_grade(list(map(int, grades)))
        students.append(create_student(firstname, lastname, marks))

    return students


def write_students_to(students: list, file) -> None:

    for student in students:
        file.write(format_info(student, 24))
        file.write("\n")


if __name__ == "__main__":
    file_to_read = open("src_14.txt", mode="r", encoding="UTF-8")
    students = read_students_from(file_to_read)
    file_to_read.close()

    print_weak_students_and_score(students)

    file_to_write = open("output_data.txt", mode="w", encoding="UTF-8")
    write_students_to(students, file_to_write)
    file_to_write.close()