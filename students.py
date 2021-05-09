class Student:
    def __init__(self, name, birthyear, birthplace):
        self.name = name
        self.birthyear = birthyear
        self.birthplace = birthplace

    def __repr__(self):
        return f'{self.name}, {self.birthyear}, {self.birthplace}'

    def __str__(self):
        return f'{self.name}, {self.birthyear}, {self.birthplace}'


students = dict()
repeat = True
temp_num = 1
while repeat:
    inp = input('define new student -> 1, exit -> done| __> ')
    if inp in ('done', 'exit'):
        break
    temp_name = f'student{temp_num}'
    temp_num += 1
    students[temp_name] = Student(input('student name: '),
                                  input('student birthday: '),
                                  input('student birthplace: '))

for std, student in students.items():
    print(std, '->', student)
