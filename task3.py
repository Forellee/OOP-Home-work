class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer) and
            course in self.courses_in_progress and
            course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        if all_grades:
            return sum(all_grades) / len(all_grades)
        return 0

    def __str__(self):
        avg = self._average_grade()
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg:.1f}\n"
            f"Курсы в процессе изучения: {in_progress}\n"
            f"Завершенные курсы: {finished}"
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() < other._average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        if all_grades:
            return sum(all_grades) / len(all_grades)
        return 0

    def __str__(self):
        avg = self._average_grade()
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {avg:.1f}"
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() < other._average_grade()


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Пример
student1 = Student('Ольга', 'Алёхина', 'жен.')
student2 = Student('Анна', 'Иванова', 'жен.')
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Пётр', 'Сидоров')
reviewer = Reviewer('Алексей', 'Смирнов')

student1.courses_in_progress += ['Python']
student2.courses_in_progress += ['Python']
student1.finished_courses += ['Git']
student2.finished_courses += ['Git']

lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']
reviewer.courses_attached += ['Python']

# Оценки
student1.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 10)
reviewer.rate_hw(student1, 'Python', 8)
reviewer.rate_hw(student2, 'Python', 9)

# Вывод
print(student1, '\n')
print(student2, '\n')
print(lecturer1, '\n')
print(lecturer2, '\n')
print(reviewer, '\n')

# Сравнения
print("student1 < student2:", student1 < student2)
print("lecturer1 < lecturer2:", lecturer1 < lecturer2)
