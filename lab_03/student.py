class Student:
    def __init__(self, name, phone, gmail, group):
        self.name = name
        self.phone = phone
        self.gmail = gmail
        self.group = group

    def __str__(self):
        return f"name: {self.name}, phone: {self.phone}, gmail: {self.gmail}, group: {self.group}"