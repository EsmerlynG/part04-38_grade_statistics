# Write your solution here
from operator import index


def get_exam_points(data):
    result = data.split()
    points = result[0]
    num_points = int(points)
    return num_points


def get_exercises_completed(data):
    result = data.split()
    exercises = result[1]
    num_exercises = int(exercises)
    return num_exercises

def points_for_exercises(exercises_list):
    e_points_list = []
    for num in exercises_list:
        e_points_list.append(num // 10)

    return e_points_list

def total_points(points_list, e_points_list):
    total_p_list = []
    i = 0
    for num in points_list:
        total_p_list.append(num + e_points_list[i])
        i += 1
    return total_p_list

def grades(t_points_list):
    grade_list = []
    for points in t_points_list:
        if 28 <= points <= 30:
            grade_list.append(5)
        elif 24 <= points <= 27:
            grade_list.append(4)
        elif 21 <= points <= 23:
            grade_list.append(3)
        elif 18 <= points <= 20:
            grade_list.append(2)
        elif 15 <= points <= 17:
            grade_list.append(1)
        else:
            grade_list.append(0)
    return grade_list

def points_avg(t_points_list):
    return sum(t_points_list) / len(t_points_list)

def pass_grades(points_list, e_points_list):

    i = 0
    passing_list = []

    for point in points_list:
        if point < 10:
            points_list[i] = 0
            e_points_list[i] = 0
        i += 1
    passing_list = total_points(points_list, e_points_list)
    return grades(passing_list)

def pass_percentage(passing_grades):
    count = 0
    for grade in passing_grades:
        if grade > 0:
            count += 1

    if count == 0:
        return f"{count:.1f}"
    else:
        pass_perc = (count / len(passing_grades)) * 100
        return f"{pass_perc:.1f}"

def grade_distribution(passing_grades):
    listed_grade = [5, 4, 3, 2, 1, 0]
    distribution_chart = ""
    for grade in listed_grade:
        grade_count = passing_grades.count(grade)
        distribution = "*" * grade_count
        distribution_chart += f"{grade}: {distribution}\n"

    return distribution_chart

def main():
    points_list = []
    exercises_list = []

    while True:
        data = input("Exam points and exercises completed: ")
        if data == "":
            break
        points_list.append(get_exam_points(data))
        exercises_list.append(get_exercises_completed(data))

    e_points_list = points_for_exercises(exercises_list)
    t_points_list = total_points(points_list, e_points_list)
    passing_grades = pass_grades(points_list, e_points_list)

    print("Statistics:")
    print(f"Points average: {points_avg(t_points_list)}")
    print(f"Pass percentage: {pass_percentage(passing_grades)}")
    print("Grade distribution:")
    print(grade_distribution(passing_grades))

main()