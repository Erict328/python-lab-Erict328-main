"""
Python Lab
CEN3031 Fall 2025

NOTE: Test data used for this lab is found in app/data.py
"""
from typing import Dict, TypedDict

class Exam(TypedDict):
   name: str
   grade: int
   comments: str

StudentDict = Dict[str, list[Exam]]

# Problem 1: Calculate a student's average grade
# 
# To complete this problem:
#   1. Find the student with the name given by `student_name`
#     a. If the student does not exist, return `0`
#   2. If the student has no exams, return 0
#   3. Calculate and return the average of all of the exams the student has taken
def calculate_student_average(students: StudentDict, student_name: str):
   """Calculate the average of all the student's exam grades
   :param students: A dictionary with students' names as keys, and a list of exam as values
   :param student_name: The name of the student to find
   :returns: The average of the student's exam grades, or 0 if not applicable
   """

   exams = students.get(student_name)
   if exams is None or len(exams) ==0:
      return 0
   total = sum(exam["grade"]for exam in exams)
   return total / len(exams)


   return 0

# Problem 2: Find the lowest and highest grades
#
# To complete this problem, find the lowest and highest grade
# in the dataset, and return these as a tuple
#
# NOTE: The tuple should be in the order (lowest, highest)
# You may assume that the list of students is never empty, but the list of exams
# for any student may be empty
def lowest_highest_grade(students: StudentDict):
   """Find the lowest and highest grade in the entire dataset

   :param students: A dictionary with students' names as keys, and a list of exams as values
   :returns: A tuple containing the lowest and highest test scores, in that order
   """
   return (-10, -5)

# Problem 3: Find teacher requests
# 
# To complete this problem, find and print data for any exam
# in the dataset that contains the word "Needs" in its "comments" field
#
# The output for each exam should look like:
# [Alice Johnson] Science Test 1 (79%): Needs improvement in lab work.
#
# Include a newline after each output
def print_feedback(students: StudentDict):
   """Print a string representing every exam where certain feedback was given

   :param students: A dictionary with students' names as keys, and a list of exams as values
   """
   pass

# Problem 4: Average across students
#
# To complete this problem, calculate the average score across all students
# for a specific test, given the test's name
def exam_average(students: StudentDict, exam_name: str):
   """Get the average score for an exam across all students

   :param students: A dictionary with students' names as keys, and a list of exams as values
   :param exam_name: The name of the exam to average the scores from
   :returns: The average score for the exam across all students
   """
   return 0

# Bonus: Report Card
#
# To complete this problem, generate and print a "report card"
# for the specified student. The report card should be comprised of
# multiple subjects, and each subject should list all exams in it
#
# To determine the subjects, use the first word in any exam's name.
# For example, "Math Test 1" is from the subject "Math"
#
# The report card should have the following header, with one empty newline below it:
# **Report Card for Alice Johnson**
#
# Each subject should look like this, with one empty newline below it:
# [Math]
#   Assignment Name      Grade    Feedback
#   Math Test 1          88       Strong understanding of concepts.
#
# NOTE: There are two spaces before each assignment name, and the table header.
# NOTE: Each column should have the following widths, with one space between each:
#         Assignment Name: 20
#         Grade: 8
#         Feedback: variable
#
# HINT: To pad a string and left-align it, use f-strings:
# `f"{var:<10}` prints the contents of `var`, pads the output with spaces to 10 characters,
#             and left-aligns the ouput
SUBJECT_HEADER = "  Assignment Name      Grade    Feedback"

def print_report_card(student_name: str, exams: list[Exam]):
   """Print a "report card" to the console for the student

   :param students_name: The name of the student
   :param exams: The list of exams the student has taken
   """
   pass