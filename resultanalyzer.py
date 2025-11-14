# Student Result Analyser Project
# Concepts: Classes, Lists, Sorting, Searching, Graph


import matplotlib.pyplot as plt
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  # list of marks
        self.total = sum(marks)
        self.percentage = self.total / len(marks)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.percentage >= 90:
            return "A+"
        elif self.percentage >= 80:
            return "A"
        elif self.percentage >= 70:
            return "B"
        elif self.percentage >= 60:
            return "C"
        elif self.percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, "
              f"Total: {self.total}, Percentage: {self.percentage:.2f}%, Grade: {self.grade}")


class StudentResultAnalyser:
    def __init__(self):
        self.students = []  # List to store student objects

    # Add student record
    def add_student(self):
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = list(map(int, input("Enter marks of 5 subjects (space-separated): ").split()))
        s = Student(roll_no, name, marks)
        self.students.append(s)
        print("✅ Student record added successfully!\n")


    def display_students(self):
        if not self.students:
            print("No records to display.\n")
            return
        print("\n------ Student Records ------")
        for s in self.students:
            s.display()
        print("-----------------------------\n")

    # Search by roll number or name
    def search_student(self):
        key = input("Enter Roll Number or Name to search: ").strip().lower()
        found = False
        for s in self.students:
            if s.roll_no.lower() == key or s.name.lower() == key:
                print("\n Student Found:")
                s.display()
                found = True
                break
        if not found:
            print("Student not found.\n")

    # Sort by percentage (Bubble Sort)
    def sort_students(self):
        n = len(self.students)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.students[j].percentage < self.students[j + 1].percentage:
                    self.students[j], self.students[j + 1] = self.students[j + 1], self.students[j]

        print("\n Sorted Student List (by Percentage):")
        for s in self.students:
            s.display()
        print()

    # Show topper
    def show_topper(self):
        if not self.students:
            print("No records available.\n")
            return
        topper = max(self.students, key=lambda x: x.percentage)
        print("\n Topper Details:")
        topper.display()
        print()

    # Class average
    def show_average(self):
        if not self.students:
            print("No records available.\n")
            return
        avg = sum(s.percentage for s in self.students) / len(self.students)
        print(f" Class Average Percentage: {avg:.2f}%\n")

    # Marks graph
    def show_graph(self):
        if not self.students:
            print("No data for graph.\n")
            return
        names = [s.name for s in self.students]
        percents = [s.percentage for s in self.students]
        plt.bar(names, percents, color='skyblue')
        plt.xlabel("Students")
        plt.ylabel("Percentage")
        plt.title("Student Performance Comparison")
        plt.show()

def main():
    system = StudentResultAnalyser()

    while True:
        print("======== STUDENT RESULT ANALYSER ========")
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Search Student")
        print("4. Sort Records by Percentage")
        print("5. Show Topper")
        print("6. Show Class Average")
        print("7. Show Graph (Bar Chart)")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.display_students()
        elif choice == '3':
            system.search_student()
        elif choice == '4':
            system.sort_students()
        elif choice == '5':
            system.show_topper()
        elif choice == '6':
            system.show_average()
        elif choice == '7':
            system.show_graph()
        elif choice == '8':
            print("Exiting... Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again!\n")


if __name__ == "__main__":
    main()
