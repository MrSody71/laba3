class Student:
    def __init__(self, name, group, age):
        self.name = name
        self.group = group
        self.age = age

    def info(self):
        return f"Студент: {self.name}, группа: {self.group}, возраст: {self.age}"

s = Student("Артюх В.В.", "221131", 20)
print(s.info())
