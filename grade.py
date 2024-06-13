class Students:
    def __init__(self):
        self.name = input("Name: ")
        self.USN = input("USN: ")
        self.Marks = []
        for i in range(5):
            self.Marks.append(int(input(f"Enter Marks of Subject {i+1}: ")))
        self.calculate_marks(self.Marks)
    def calculate_marks(self, marks):
        self.total_marks = sum(marks)
        self.percentage = (self.total_marks/500)*100
        self.grade = "A" if self.percentage > 70 else "B"
    def display(self):
        print(f"Name:{self.name} USN:{self.USN} Marks:{self.total_marks} Grade:{self.grade} Score:{self.percentage}.%2f")
stu = [0] * 2
for i in range(2):
    stu[i] = Students()
for i in range(2):
    stu[i].display()
