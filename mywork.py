import pandas as pd
students_work= pd.read_csv('student_data.csv')
print(students_work)
print(students_work.head())
print(students_work.describe())
print(students_work.info())

students_work.duplicated().sum()
print(students_work.duplicated().sum())

students_work.isnull().sum()
print(students_work.isnull().sum())

# explore relationship: to find out if studytime affect grade performance
study_time_grade_per= students_work[['studytime', 'G3']].corr()
print(study_time_grade_per)

# absences affect grade performance
absences_grade_per= students_work[['absences', 'G3']].corr()
print(absences_grade_per)

# comparing students by category
students_gender_performance= students_work.groupby('sex')['G3'].mean()
print(students_gender_performance)# male performs exceedingly than the female

# school supports by grade
grade_sch_support= students_work.groupby('schoolsup')['G3'].mean()
print(grade_sch_support)# school supports doesn't contribute to grade performance

import matplotlib.pyplot as plt
plt.scatter(students_work['studytime'], students_work['G3'])
plt.xlabel('Study Time')
plt.ylabel('Final Grade (G3)')
plt.show()

plt.scatter(students_work['absences'], students_work['G3'])
plt.xlabel('Absences')
plt.ylabel('Final Grade (G3)')
plt.show()