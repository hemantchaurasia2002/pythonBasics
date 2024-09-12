people = [
    {"name": "Deadshot", "role": "support"},
    {"name": "Monster", "role": "igl"},
    {"name": "Wizard", "role": "assulture"},
    {"name": "Phoenix", "role": "filter assulture"}
]

people.sort(key=lambda person:["name"])

print(people)