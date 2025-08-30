students = [("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 85), ("Eve", 78), ("Frank", 85), ("Mark", 50), ("George", 21)]

##Unique Grades: Extract and print all the unique grades from the list of student scores.

grades = [score for name, score in students]
unique_grades = set(grades)
print("Unique Grades:", unique_grades)

##Top Performers: Identify and print the names of the top three students with the highest scores.
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
top_three = sorted_students[:3]
top_names = [name for name, score in top_three]
print("Top Performers:", top_names)

##Failed Students: Identify and print the names of students who scored below 51, along with their scores.
failed_students = [(name, score) for name, score in students if score < 51]
print("Failed Students:", failed_students)