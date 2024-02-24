# Problem Set - 2
# For the next Problem set, You’re going to insert a student’s grade score into a dictionary. 
# So given a integer as the number of students. Use the for loop to insert the student’s data name and grade.
# So at the end you would have a dictionary like this:
# Case when the input number is 5
# grade = {'Ceb': 90, 'Sebastian': 80, 'Popowi': 80, 'Janggar': 75, 'Proboro': 85}

def create_student_grade_dictionary(num_students):
    dictionary = {}  # Initialize an empty dictionary

    for _ in range(num_students):
        name = input("Enter student name: ")
        grade = int(input("Enter student grade: "))
        dictionary[name] = grade # Insert the student's name and grade into the dictionary

    return grade

num_students = int(input("Enter the number of students: "))
result_dictionary = create_student_grade_dictionary(num_students)
print("grade = ", result_dictionary)