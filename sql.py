import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
Create table STUDENT(NAME VARCHAR(25), ROLE VARCHAR(25), COMPANY VARCHAR(25), LOCATION VARCHAR(25), SALARY INT)
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Aneesh', 'Product Management Intern', 'Juniper Networks', 'Sunnyvale', 60)''')
cursor.execute('''Insert Into STUDENT values('Manohar', 'Machine Learning Engineer Intern', 'Apple', 'Seattle', 52)''')
cursor.execute('''Insert Into STUDENT values('Abhinav', 'Software Engineer Intern', 'Oracle', 'Redwood City', 50)''')
cursor.execute('''Insert Into STUDENT values('Aadesh', 'Deep Learning Architect Intern', 'NVIDIA', 'Santa Clara', 54)''')
cursor.execute('''Insert Into STUDENT values('Hariharan', 'Data Science Intern', 'Quorvo', 'Dallas', 45)''')

print("The inserted records are")

data = cursor.execute('''Select * FROM STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()

