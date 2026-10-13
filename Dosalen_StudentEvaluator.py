#Name: Evan Jane L. Dosalen
#Date: October 13, 2026
#Program: This program evaluates a student's performance.

name = input("Enter Student Name: ")
assessment_score_1 = int(input("Enter your assessment score 1: "))
assessment_score_2 = int(input("Enter your assessment score 2: "))
assessment_score_3 = int(input("Enter your assessment score 3: "))

def display_header():
    print("=============================================================")
    print("Student Performance Evaluator")
    print("=============================================================")

def get_student_info():
    print(name)
    print(assessment_score_1)
    print(assessment_score_2)
    print(assessment_score_3)

assessment_score = (assessment_score_1+assessment_score_2+assessment_score_3)

def evaluate_performance():
    print("Average: ", assessment_score)


def display_results():
    print(name)
    print(assessment_score_1)
    print(assessment_score_2)
    print(assessment_score_3)

