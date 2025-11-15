import calendar
import random

numbers_of_birthdays = int(input("How many birthdays shall I generate? (100 max): "))

birthdays = []

for birthday in range(numbers_of_birthdays):
    random_month = random.randint(1, 12)
    month = calendar.month_abbr[random_month]
    max_date = calendar.monthrange(2025, random_month)
    date = random.randint(1, max_date[1])
    birthday = f"{month}, {date}"
    birthdays.append(birthday)


