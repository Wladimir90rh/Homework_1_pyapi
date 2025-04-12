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


best_student = Student('Donald', 'Trump', 'M')
best_student.courses_in_progress += ['Python']

bad_student = Student('Peter', 'Pan', 'M')
bad_student.courses_in_progress += ['Python']

foolish_student = Student('Homer', 'Simpson', 'M')
foolish_student.courses_in_progress += ['Java']
 
cool_lector = Lecturer('Ilon', 'Musk')
cool_lector.courses_attached += ['Python']
cool_lector.courses_attached += ['Java']

bad_lector = Lecturer('Olga', 'Buzova')
bad_lector.courses_attached += ['Python']
bad_lector.courses_attached += ['Java']

cool_lector.receive_grade(best_student, 'Python', 5)
cool_lector.receive_grade(bad_student, 'Python', 5)
cool_lector.receive_grade(foolish_student, 'Java', 4)

bad_lector.receive_grade(best_student, 'Python', 4)
bad_lector.receive_grade(bad_student, 'Python', 5)
bad_lector.receive_grade(foolish_student, 'Java', 5)

cool_reviewer = Reviewer('Ilon', 'Musk')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(bad_student, 'Python', 2)
cool_reviewer.rate_hw(foolish_student, 'Java', 2)

print(best_student)
print(cool_lector)
print(cool_reviewer)

print(best_student == bad_student)
print(bad_student == foolish_student)
print(cool_lector == bad_lector)