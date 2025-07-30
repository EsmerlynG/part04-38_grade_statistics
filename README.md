# Grade Statistics Program

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A mini-project completed as part of the [MOOC.fi Python Programming course](https://programming-22.mooc.fi/).
The program reads student course results and outputs grade statistics based on defined rules.

---

## 🚀 Features

* Collects **exam points** and **number of exercises completed** from multiple students.
* Converts exercises to points and applies grading logic.
* Outputs:
  * **Points average**
  * **Pass percentage**
  * **Grade distribution (0–5)**

---

## 📊 Grading Rules

* **Exercise points**: For every 10% of exercises completed, the student gets 1 point (max 10).
* **Final grade**: Based on total points (exam + exercise points):

| Total Points | Grade    |
| ------------ | -------- |
| 0–14         | 0 (fail) |
| 15–17        | 1        |
| 18–20        | 2        |
| 21–23        | 3        |
| 24–27        | 4        |
| 28–30        | 5        |

* **Cut-off**: If exam points are less than 10, the student automatically fails.

---

## 🧠 Approach & Pseudocode

I started by planning the structure using pseudocode:

```
1. Start program
2. While true:
      ask for "exam points and exercises completed"
      if empty line -> stop input
      extract exam points and exercises
      store them in separate lists
3. Convert exercises to exercise points (// 10)
4. Combine exam points and exercise points into total points
5. Apply fail rule for exams < 10 (set points to 0)
6. Calculate:
      - grades for each student
      - points average
      - pass percentage
      - grade distribution
7. Print results in required format
8. End program
```

---

## 🧩 Program Structure

Main functions:

* `get_exam_points(data)`
* `get_exercises_completed(data)`
* `points_for_exercises(exercises_list)`
* `total_points(points_list, e_points_list)`
* `grades(t_points_list)`
* `points_avg(t_points_list)`
* `pass_grades(points_list, e_points_list)`
* `pass_percentage(passing_grades)`
* `grade_distribution(passing_grades)`
* `main()`

Each function was implemented and tested separately before being integrated.

---

## 🖥️ Sample Input / Output

**Input:**

```
Exam points and exercises completed: 15 87
Exam points and exercises completed: 10 55
Exam points and exercises completed: 11 40
Exam points and exercises completed: 4 17
Exam points and exercises completed:
```

**Output:**

```
Statistics:
Points average: 14.5
Pass percentage: 75.0
Grade distribution:
5:
4:
3: *
2:
1: **
0: *
```

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 main.py
```

Follow the prompts to enter student data.

---

## ✨ Lessons Learned

* Writing pseudocode first made the logic clearer.
* Breaking the program into functions simplified testing and debugging.
* Strengthened understanding of loops, list manipulation, and conditionals in Python.

---

## 🔍 Reflection

While this program works as intended, I plan to make the following improvements:

* **Refactor the `grades()` function:**
  The grading logic currently uses multiple `if/elif` statements.
  I intend to make it **more readable and maintainable** using a cleaner structure such as mapping ranges to grades.

This will make the codebase more professional as I revisit it in the future.

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
