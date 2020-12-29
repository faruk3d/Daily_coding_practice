# code challenge 1
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
    print(student_scores[name])
    if 91 <= student_scores[name] <= 100:
        student_grades[name] = "Outstanding"
    elif 81 <= student_scores[name] <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif 71 <= student_scores[name] <= 80:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)
