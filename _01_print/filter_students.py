#Filter students with 2 or more lessons
#Autor: Bella
students = {
    "Аня": 2,
    "Миша": 3,
    "Дима": 1
}
for name, lessons in students.items():
    if lessons>=2:
        print(name)
