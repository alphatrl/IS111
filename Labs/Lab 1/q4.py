# Created by Amos Tan for students to reference their lab work
# Q4

# Constants
TOTAL_SCORE_ASSIGNMENT = 10
TOTAL_SCORE_TEST_1 = 30
TOTAL_SCORE_TEST_2 = 40
TOTAL_SCORE_EXAM = 140

CUMULATIVE_ASSIGNMENT = 0.1
CUMULATIVE_TEST_1 = 0.15
CUMULATIVE_TEST_2 = 0.2
CUMULATIVE_EXAM = 0.35

# Get variables
ass1Score = float(input("What's your score for Assignment 1? "))
ass2Score = float(input("What's your score for Assignment 2? "))
ass3Score = float(input("What's your score for Assignment 3? "))
test1Score = float(input("What's your score for Test 1? "))
test2Score = float(input("What's your score for Test 2? "))
examScore = float(input("What's your score for the Exam? "))


# calculate
ass1 = (ass1Score / TOTAL_SCORE_ASSIGNMENT) * CUMULATIVE_ASSIGNMENT
ass2 = (ass2Score / TOTAL_SCORE_ASSIGNMENT) * CUMULATIVE_ASSIGNMENT
ass3 = (ass3Score / TOTAL_SCORE_ASSIGNMENT) * CUMULATIVE_ASSIGNMENT
test1 = (test1Score / TOTAL_SCORE_TEST_1) * CUMULATIVE_TEST_1
test2 = (test2Score / TOTAL_SCORE_TEST_2) * CUMULATIVE_TEST_2
exam = (examScore / TOTAL_SCORE_EXAM) * CUMULATIVE_EXAM

# final results
finalScore = (ass1 + ass2 + ass3 + test1 + test2 + exam) * 100
print(f"Your final cumulative score is {finalScore} / 100")