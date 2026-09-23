# ==========================================
#       COLLEGE MANAGEMENT SYSTEM
# ==========================================


# Parent Class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Age  :", self.age)


# Student Class
class Student(Person):

    def __init__(self, student_id, name, age, branch, year):
        super().__init__(name, age)

        self.student_id = student_id
        self.branch = branch
        self.year = year

    def display(self):
        print("----------------------------")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Branch     :", self.branch)
        print("Year       :", self.year)
        print("----------------------------")


# Teacher Class
class Teacher(Person):

    def __init__(self, teacher_id, name, age, subject):
        super().__init__(name, age)

        self.teacher_id = teacher_id
        self.subject = subject

    def display(self):
        print("----------------------------")
        print("Teacher ID :", self.teacher_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Subject    :", self.subject)
        print("----------------------------")


# Course Class
class Course:

    def __init__(self, course_id, course_name, duration):
        self.course_id = course_id
        self.course_name = course_name
        self.duration = duration

    def display(self):
        print("----------------------------")
        print("Course ID  :", self.course_id)
        print("Course     :", self.course_name)
        print("Duration   :", self.duration)
        print("----------------------------")


# College Management Class
class CollegeManagement:

    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []


    # ==============================
    # Add Student
    # ==============================

    def add_student(self):

        print("\n===== ADD STUDENT =====")

        student_id = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        branch = input("Enter Branch: ")
        year = input("Enter Year: ")

        student = Student(
            student_id,
            name,
            age,
            branch,
            year
        )

        self.students.append(student)

        print("\nStudent added successfully!")


    # ==============================
    # Add Teacher
    # ==============================

    def add_teacher(self):

        print("\n===== ADD TEACHER =====")

        teacher_id = int(input("Enter Teacher ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        subject = input("Enter Subject: ")

        teacher = Teacher(
            teacher_id,
            name,
            age,
            subject
        )

        self.teachers.append(teacher)

        print("\nTeacher added successfully!")


    # ==============================
    # Add Course
    # ==============================

    def add_course(self):

        print("\n===== B.TECH SPECIALIZATIONS =====")

        print("1. CSE")
        print("2. ECE")
        print("3. EEE")
        print("4. Mechanical Engineering")
        print("5. Civil Engineering")
        print("6. AI & Data Science")
        print("7. AI & Machine Learning")
        print("8. Information Technology")

        choice = int(input("Select Specialization: "))


        if choice == 1:
            course_name = "B.Tech CSE"

        elif choice == 2:
            course_name = "B.Tech ECE"

        elif choice == 3:
            course_name = "B.Tech EEE"

        elif choice == 4:
            course_name = "B.Tech Mechanical Engineering"

        elif choice == 5:
            course_name = "B.Tech Civil Engineering"

        elif choice == 6:
            course_name = "B.Tech AI & Data Science"

        elif choice == 7:
            course_name = "B.Tech AI & Machine Learning"

        elif choice == 8:
            course_name = "B.Tech Information Technology"

        else:
            print("Invalid specialization!")
            return


        course_id = len(self.courses) + 301

        course = Course(
            course_id,
            course_name,
            "4 Years"
        )

        self.courses.append(course)

        print("\nCourse added successfully!")
        print("Course ID :", course_id)
        print("Course    :", course_name)
        print("Duration  : 4 Years")


    # ==============================
    # Display Students
    # ==============================

    def display_students(self):

        print("\n===== STUDENTS =====")

        if len(self.students) == 0:

            print("No students found.")
            return


        for student in self.students:

            student.display()


    # ==============================
    # Display Teachers
    # ==============================

    def display_teachers(self):

        print("\n===== TEACHERS =====")

        if len(self.teachers) == 0:

            print("No teachers found.")
            return


        for teacher in self.teachers:

            teacher.display()


    # ==============================
    # Display Courses
    # ==============================

    def display_courses(self):

        print("\n===== COURSES =====")

        if len(self.courses) == 0:

            print("No courses found.")
            return


        for course in self.courses:

            course.display()


    # ==============================
    # Search Student
    # ==============================

    def search_student(self):

        print("\n===== SEARCH STUDENT =====")

        student_id = int(
            input("Enter Student ID: ")
        )


        for student in self.students:

            if student.student_id == student_id:

                print("\nStudent Found!")

                student.display()

                return


        print("Student not found.")


    # ==============================
    # Main Menu
    # ==============================

    def menu(self):

        while True:

            print("\n")
            print("===================================")
            print("       COLLEGE MANAGEMENT SYSTEM")
            print("===================================")

            print("1. Add Student")
            print("2. Add Teacher")
            print("3. Add Course")
            print("4. Display Students")
            print("5. Display Teachers")
            print("6. Display Courses")
            print("7. Search Student")
            print("8. Exit")


            choice = int(
                input("Enter your choice: ")
            )


            if choice == 1:

                self.add_student()


            elif choice == 2:

                self.add_teacher()


            elif choice == 3:

                self.add_course()


            elif choice == 4:

                self.display_students()


            elif choice == 5:

                self.display_teachers()


            elif choice == 6:

                self.display_courses()


            elif choice == 7:

                self.search_student()


            elif choice == 8:

                print("\nThank you for using College Management System!")

                break


            else:

                print("\nInvalid choice! Please try again.")


# ==========================================
# Create Object
# ==========================================

college = CollegeManagement()

college.menu()