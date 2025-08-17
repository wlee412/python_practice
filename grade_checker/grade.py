student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90 : 
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)