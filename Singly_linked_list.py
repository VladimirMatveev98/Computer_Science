class Student():
    def __init__(self,name,age,gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        str_res = str(self.name) + ", " + str(self.age) + ", " + str(self.gpa)
        return str_res

    def get_age(self):
        return self.age

    def get_gpa(self):
        return self.gpa

class Singly_linked_list():
    def __init__(self,data):
        self.data = data
        self.next = None

    def append(self,data):
        end = Singly_linked_list(data)
        while self.next:
            self = self.next
        self.next = end

    def print_list(self):
        print(self.data)
        while self.next:
            self = self.next
            print(self.data)

    def search_name(self, name):
        if self.data.name == name:
            print("Студент есть в списке!")
            return True
        while self.next:
            if self.data.name == name:
                print("Студент есть в списке!")
                return True
            self = self.next
        return False

    def return_all(self):
        res_list = []
        if self.data:
            res_list.append(self.data)
            while self.next:
                self = self.next
                res_list.append(self.data)
        return res_list

    def print_by_age(self):
        list_2 = list_1.return_all()
        list_2.sort(key = sort_by_age)
        for student in list_2:
            print(student)

    def print_by_gpa(self):
        list_2 = list_1.return_all()
        list_2.sort(key = sort_by_gpa)
        for student in list_2:
            print(student)

def sort_by_age(student):
    return student.get_age()

def sort_by_gpa(student):
    return student.get_gpa()


student_1 = Student("Николай", 22, 4.5)
student_2 = Student("Василий", 20, 4.4)
student_3 = Student("Владимир", 24, 4.6)
student_4 = Student("Максим", 25, 4.8)
student_5 = Student("Даниил", 21, 3.9)


list_1 = Singly_linked_list(student_1)
list_1.append(student_2)
list_1.append(student_3)
list_1.append(student_4)
list_1.append(student_5)
list_1.print_list()
print('\n')
list_1.search_name("Максим") #Студент есть в списке!

print('\nСортировка по возрасту:')
list_1.print_by_age()


print('\nСортировка по среднему баллу:')
list_1.print_by_gpa()
