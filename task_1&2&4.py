class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
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



best_student = Student('Donald', 'Trump', 'M')
best_student.courses_in_progress += ['Python']

bad_student = Student('Peter', 'Pan', 'M')
bad_student.courses_in_progress += ['Python']

foolish_student = Student('Homer', 'Simpson', 'M')
foolish_student.courses_in_progress += ['Java']
 
cool_lector = Lecturer('Ilon', 'Musk')
cool_lector.courses_attached += ['Python']
cool_lector.courses_attached += ['Java']

cool_lector.receive_grade(best_student, 'Python', 5)
cool_lector.receive_grade(bad_student, 'Python', 2)
cool_lector.receive_grade(foolish_student, 'Java', 3)

cool_reviewer = Reviewer('Ilon', 'Musk')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 5)

print(cool_lector.grades)
print(best_student.grades)