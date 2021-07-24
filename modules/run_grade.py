"""
Script for processing a student grades.
"""

from grades.predict import predict_score
from grades.result import get_grade

score_history = [50, 90, 70, 100]
predicted_score = predict_score(score_history, 50)
predicted_grade = get_grade(predicted_score)

print(f'The student predicted grade is: {predicted_grade}')