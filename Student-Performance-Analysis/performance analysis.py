import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv("student_performance.csv")
df
#avg marks of each subject
avg_marks=df[['Maths','English','Science']].mean()

#finding topper
df['Total']=df['Maths']+df['English']+df['Science']
df[['Name','Total']]
df.loc[df['Total'].idxmax()]
'''
avg_marks.plot(kind='bar')
plt.title("Avg marks per subject")
plt.ylabel("Marks")
plt.show()

#attendance v/s total marks
plt.scatter(df['Attendance'],df['Total'])
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.title("Attendance v/s Marks")
plt.show()
'''
#Grade classification
'''df['Total']
def assign_grade(Total):
    if Total>= 240:
        return 'A'
    elif Total>=180:
        return 'B'
    else:
        return 'C'
df['Grade']=df['Total'].apply(assign_grade)

print(df[['Name','Total','Grade']])'''

#Pass or fail analysis
df['Result']=df['Total'].apply(lambda x: 'Pass' if x>=170 else 'Fail')
print(df[['Name','Total','Result']])