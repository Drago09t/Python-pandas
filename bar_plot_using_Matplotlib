import pandas as pd
 import matplotlib.pyplot as plt
 data = {
 'Student_ID': [1, 2, 4],
 'Exam_Score': [85, 90, 92],
 'Grade': ['A', 'B', 'A']
 }
 df_cleaned = pd.DataFrame(data)
 grade_counts = df_cleaned['Grade'].value_counts()
 plt.bar(grade_counts.index, grade_counts.values, color='blue')
 plt.xlabel('Grade')
 plt.ylabel('Number of Students')
 plt.title('Distribution of Grades Among Students')
 plt.show()
