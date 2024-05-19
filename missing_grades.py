import pandas as pd
 data = {
 'Student_ID': [1, 2, 3, 4, 5],
 'Exam_Score': [85, 90, 78, 92, 87],
 'Grade': ['A', 'B', None, 'A', None]
 }
 df = pd.DataFrame(data)
 cleanData = df.dropna(subset=['Grade'])
 print("Cleaned DataFrame:")
 print(cleanData
