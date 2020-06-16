'''
HackerLand University has the following grading policy:
Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:
If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
For example,grade=84  will be rounded to 85 but grade=29 will not be rounded because the rounding would result in a number that is less than 40.
Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.

Input Format:
The first line contains a single integer, n, the number of students.
Each line i of the n subsequent lines contains a single integer, garde[i], denoting student i's grade.

Constraints:
1 <= n <= 60 and 0 <= grade[i] <= 100

Output Format:
For each grade[i], print the rounded grade on a new line.
'''



import math
import os
import random
import re
import sys

def gradingStudents(grades):
    x = []
    for grade in grades:
        g = str(grade)
        if int(g[-1])>=3 and int(g[-1])<=5 and int(g)>=38:
            x.append(g[:-1]+'5')
        elif int(g[-1])>7 and int(g[-1])<10 and int(g)>=38:
            x.append(str(int(g[:-1])+1)+'0')
        else:
            x.append(g)
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
