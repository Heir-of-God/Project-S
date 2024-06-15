import os


def round_grade(grade):
    remainders_add = {1: 0, 2: 0, 3: 2, 4: 1, 0: 0}
    if grade < 38:
        return grade
    return grade + remainders_add[grade % 5]


def gradingStudents(grades):
    for ind in range(len(grades)):
        grades[ind] = round_grade(grades[ind])
    return grades


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
