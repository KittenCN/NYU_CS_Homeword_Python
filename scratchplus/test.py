class students:
    def __init__(self, name, age, score1, score2, score3, score4, score5):
        self.name = name
        self.age = age
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.score4 = score4
        self.score5 = score5

menu = "1. Add student\n2. Serching student\n3. Exit"
intChoose = -1
student = []
while intChoose != 3:
    print(menu)
    intChoose = int(input("Choose: "))
    if intChoose == 1:
        name = input("Name: ")
        age = int(input("Age: "))
        score1 = int(input("Score 1: "))
        score2 = int(input("Score 2: "))
        score3 = int(input("Score 3: "))
        score4 = int(input("Score 4: "))
        score5 = int(input("Score 5: "))
        student.append(students(name, age, score1, score2, score3, score4, score5))
    elif intChoose == 2:
        studentname = input("Student name: ")
        for i in range(len(student)):
            if studentname == student[i].name:
                print("Name: ", student[i].name + "\r\n" + "Age: ", str(student[i].age) + "\r\n" + "Score 1: ", str(student[i].score1) + "\r\n" + "Score 2: ", str(student[i].score2) + "\r\n" + "Score 3: ", str(student[i].score3) + "\r\n" + "Score 4: ", str(student[i].score4) + "\r\n" + "Score 5: ", str(student[i].score5) + "\r\n" + "Average: ", str((student[i].score1 + student[i].score2 + student[i].score3 + student[i].score4 + student[i].score5) / 5) + "\r\n" + "Grade: ", str(student[i].score1 + student[i].score2 + student[i].score3 + student[i].score4 + student[i].score5))
                print("")
    elif intChoose == 3:
        break
    else:
        print("Wrong choose!")
        print("")
        continue
