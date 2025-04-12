class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __mean_grade(self):
        if len(self.grades):
            all_grades = []
            for grades in self.grades.values():
                for grade in grades:
                    all_grades.append(grade)
            self.__mgrade = round(sum(all_grades) / len(all_grades), 2)
        else:
            self.__mgrade = 0
        return self.__mgrade

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.__mean_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')
    
    def __eq__(self, second_student):
        if isinstance(second_student, Student):
            return self.__mean_grade() == second_student.__mean_grade()
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def receive_grade(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and (course in student.courses_in_progress or course in student.finished_courses):
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __mean_grade(self):
        if len(self.grades):
            all_grades = []
            for grades in self.grades.values():
                for grade in grades:
                    all_grades.append(grade)
            self.__mgrade = round(sum(all_grades) / len(all_grades), 2)
        else:
            self.__mgrade = 0
        return self.__mgrade
    
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.__mean_grade()}\n')
    
    def __eq__(self, second_lecturer):
        if isinstance(second_lecturer, Lecturer):
            return self.__mean_grade() == second_lecturer.__mean_grade()
        else:
            return 'Ошибка'


student_1 = Student('Donald', 'Trump', 'M')
student_1.courses_in_progress += ['Python']
student_2 = Student('Peter', 'Pan', 'M')
student_2.courses_in_progress += ['Python']

lecturer_1 = Lecturer('Ilon', 'Musk')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Elon', 'Musk')
lecturer_2.courses_attached += ['Python']

reviewer_1 = Reviewer('Mark', 'Zuckerberg')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Jeff', 'Bezos')
reviewer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_2, 'Python', 1)
reviewer_2.rate_hw(student_1, 'Python', 5)

lecturer_1.receive_grade(student_1, 'Python', 5)
lecturer_1.receive_grade(student_2, 'Python', 3)
lecturer_2.receive_grade(student_1, 'Python', 4)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
print(student_1 == student_2)
print(lecturer_1 == lecturer_2)


def average_grade_students(students, course):
    total_grades = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            count += len(student.grades[course])
    if count == 0:
        return 0
    return round(total_grades / count, 2)


def average_grade_lecturers(lecturers, course):
    total_grades = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    if count == 0:
        return 0
    return round(total_grades / count, 2)


students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]

print(average_grade_students(students, 'Python'))
print(average_grade_lecturers(lecturers, 'Python'))