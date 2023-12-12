import re

with open("yousef.txt", "r") as file:
    text = file.read().strip()

pattern = re.compile(r"[A-z0-9._]+@[A-z0-9._]+\.\w+")
emails = pattern.finditer(text)

for i in emails:
    print("Emails => " + i.group())

pattern = re.compile(r"\d{3}(\s|-)?\d{4}(\s|-)?\d{4}")
phones = pattern.finditer(text)

for j in phones:
    print("Phone numbers => " + j.group())


pattern = re.compile(r"^[A-z]+\s[A-z]+\s[A-z]+",re.MULTILINE)
names = pattern.finditer(text)

for k in names:
    print("Names => " + k.group())
