import calendar
import random

numbers_of_birthdays = int(input("How many birthdays shall I generate? (100 max): "))
birthdays = {}
max_count = 0
most_common = ''
simulated_birthdays = 0

for birthday in range(numbers_of_birthdays):
    random_month = random.randint(1, 12)
    month = calendar.month_abbr[random_month]
    max_date = calendar.monthrange(2025, random_month)
    date = random.randint(1, max_date[1])
    birthday = f"{month} {date}"
    if birthday in birthdays:
        birthdays[birthday] += 1
    else:
        birthdays[birthday] = 1
    
for key, value in birthdays.items():
    if value > max_count:
        max_count = value
        most_common = key

print(f"Here are {numbers_of_birthdays} birthdays:")
for b in birthdays:
    print(b, end=', ')
print()
print(f"Multiple people have a birthday on {most_common}")
print(f"Generating {numbers_of_birthdays} random birthdays 100,000 times...")
begin_simulation = input("Press Enter to begin...")
print("Let's run another 100,000 simulations")
print("0 percent done")


simulation = 0
while simulation < 100000:
    birthdays = {}
    simulation += 1
    if simulation == 25000:
        print("25 percent done")
    if simulation == 50000:
        print("50 percent done")
    if simulation == 75000:
        print("75 percent done")
    for birthday in range(numbers_of_birthdays):
        random_month = random.randint(1, 12)
        month = calendar.month_abbr[random_month]
        max_date = calendar.monthrange(2025, random_month)
        date = random.randint(1, max_date[1])
        birthday = f"{month} {date}"
        if birthday in birthdays:
            birthdays[birthday] += 1
        else:
            birthdays[birthday] = 1
    for value in birthdays.values():
        if value > 1:
            simulated_birthdays += 1
            break
print("100 percent done")
print(f"Out of 100,000 simulations of {numbers_of_birthdays} people, there was a matching birthday in that group {simulated_birthdays} times. This means that {numbers_of_birthdays} people have a {(simulated_birthdays / 100000) * 100} percent chance of having a matching birthday in their group")





        
            

    








