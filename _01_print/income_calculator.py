students={
    "Аня": 2,
    "Миша": 3,
    "Дима": 1
}
total=0
price=300
for name, lessons in students.items():
    income=lessons*price
    print(f"{name}: {income} руб/нед")
    total+=income
print('Итого за неделю:', total )
print('Итого за месяц:', total*4)
