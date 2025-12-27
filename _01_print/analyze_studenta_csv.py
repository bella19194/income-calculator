#Analyze students data from CSV
#Author: Sabira

import csv

total_lessons = 0
max_lessons = 0
top_student = ''

with open("students.cvs", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        name = row[0]
        lessons = int(row[1])
        total_lessons+=lessons
        if max_lessons<lessons:
            max_lessons=lessons
            top_student=name

print('Всего уроков:', total_lessons )
print('Больше всего уроков у:', top_student)


