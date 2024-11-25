students = [
    ("Oil", "CS-1", "oil@gmail.com"),
    ("Bob", "CS-2", "bob@gmail.com"),
    ("Marta", "CS-2", "marta@gmail.com"),
    ("Dima", "CS-2", "dima@gmail.com"),
    ("Eve", "CS-1", "eve@gmail.com"),
    ("Zoe", "CS-2", "zoe@gmail.com"),
    ("Josh", "CS-1", "josh@gmail.com"),
]

sortStudents = sorted(students, key=lambda x: (x[1], x[0]))

print("Відсортований список студентів:")
groupBig = None
for student in sortStudents:
    name, group, gmail = student
    if group != groupBig:
        print(f"\nГрупа {group}:")
        groupBig = group
    print(f"   {name} - {gmail}")