# Export students data to CSV
# Sabira

import csv
students = {
    'Аня': 2,
    'Миша': 3,
    'Дима': 1
}
with open("students.cvs", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "lessons"])

    for name, lessons in students.items():
        writer.writerow([name, lessons])






