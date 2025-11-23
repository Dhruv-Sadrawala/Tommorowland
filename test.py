def three(a,b,c):
    if a >= b and a >= c:
        return a
    elif b>= a and b>= c:
        return b
    else:
        return c

a = int(input("Enter one number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

res = three(a,b,c)

print("Greatest is:",res)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ian', 'Jack', 'Kiran', 'Lily', 'Mohan', 'Nina', 'Oscar', 'Priya', 'Quinn', 'Ravi', 'Sara', 'Tom'],
    # A value for Age is missing for Charlie.
    'Age': [25, 30, np.nan, 40, 29, 33, 35, 35, 45, 38, 31, 28, 36, 42, 34, 34, 39, 41, 27, 32],
    'Department': ['HR', 'Finance', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'Finance', 'IT', 'Finance', 'HR', 'IT', 'HR', 'Finance'],
    # Salary values are missing for Eva and Lily.
    'Salary': [50000, 60000, 70000, 80000, np.nan, 75000, 62000, 55000, 90000, 68000, 72000, np.nan, 58000, 64000, 78000, 81000, 56000, 87000, 52000, 66000],
    'Experience_Years': [2, 5, 3, 10, 3, 7, 6, 3, 12, 8, 4, 3, 3, 11, 7, 9, 4, 13, 2, 5],
    'Performance_Score': [3, 4, 5, 4, 4, 5, 4, 3, 5, 4, 4, 6, 5, 4, 5, 4, 4, 5, 2, 5],
    'Joining_Date': pd.to_datetime(['2020-01-15', '2019-03-20', '2021-07-10', '2018-05-25', '2020-09-01', '2022-01-10', '2021-03-15', '2019-06-12', '2018-11-05', '2020-12-30', '2019-08-22', '2021-09-11', '2020-04-15', '2018-03-10', '2022-07-20', '2019-10-01', '2020-06-18', '2017-05-05', '2021-11-11', '2019-12-25'])
}

df = pd.DataFrame(data)
print("="*50)
print(df)
print("="*50)

print("="*50)
print("Data Frame Info")
print("="*50)
print("Quantile 25% : ",df['Salary'].quantile(0.25))
print(df.dtypes)


print("="*50)
print("After Alteration")
print("="*50)
print(df.dropna().rename(columns={'Salary':'Remuneration'}))

data = {
    'Full Name': ['Alice Johnson', 'Bob Smith', None, 'Charlie Brown'],
    'Email': ['alice@abc.com', 'bob@xyz.com', 'invalid_email', 'charlie@abc.com']
    }

df = pd.DataFrame(data)

df[['FN','LN']] = df['Full Name'].str.split(' ',expand=True)
print(df)


data = ['Jan','Feb','Mar']
points = [12,30,47]

plt.plot(data,points,marker='o',color='green')
plt.bar(data, points, color=["blue", "green", "orange"])
plt.pie(points,labels=data,explode=[0,0,0.1])

plt.title("Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales(in Cr.)")
plt.grid()
plt.show()

dates = pd.date_range(start="2023-01-01", periods=12, freq="M")
sales = [100, 120, 130, 140, 150, 160, 155, 165, 175, 180, 190, 200]

plt.plot(dates, sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()