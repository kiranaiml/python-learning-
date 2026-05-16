#The PUC Mock Exam Grader
bs_mock_scores=[15,42,38,12,49,17]
passing_percentage=[scores*2 for scores in bs_mock_scores if scores>17]
print(passing_percentage)
