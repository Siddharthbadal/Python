print("Welcome to the grade Sorter App")
grades = []
print()

grade = int(input("\nWhat is your first grade (0-100): "))
grades.append(grade)
grade = int(input("What is your first grade (0-100): "))
grades.append(grade)
grade = int(input("What is your first grade (0-100): "))
grades.append(grade)
grade = int(input("What is your first grade (0-100): "))
grades.append(grade)

print()
print("your gardes are: ", str(grades))

grades.sort(reverse=True)
print("Your grade from highest to lowest: ", grades)
print()
print("The lowest two grades will now be dropped.")
min1 = grades.pop(3)
min2 = grades.pop(2)
print("Removed grade: ",  min1)
print("Removed grade: ", min2)
print()
print("Your remaining grades:", grades)
print("Good Job! Your highest grade is a", max(grades))
