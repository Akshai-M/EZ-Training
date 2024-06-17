class Students:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
std1 = Students('Akshai',20,'M')
std1 = Students()
print(std1.name,std1.age,std1.gender)


class Students1:
    def __init__(self):
        self.name = 'Kumar'
        self.age = 19
        self.gender = 'Male'

    def display(self):
        print(self.name,self.age,self.gender)
std2 = Students1()
std2.display()
# print(std1.name,std1.age,std1.gender)