# not allowed to use min() or max()

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_value = 0
for score in student_scores:
  if score > highest_value:
    highest_value = score

print(f"The highest score in the class is: {highest_value}")