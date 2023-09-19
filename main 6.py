class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of student objects by CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage:
if __name__ == "__main__":
    # Creating a list of student objects
    students = [
        Student("Alice", "A101", 3.9),
        Student("Bob", "B102", 3.7),
        Student("Charlie", "C103", 3.8),
        Student("David", "D104", 4.0),
    ]

    # Sorting the list of students by CGPA
    sorted_students = sort_students(students)

    # Printing the sorted list
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")