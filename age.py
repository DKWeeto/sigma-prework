def age(input_date):
    from datetime import date, datetime
    today = date.today()
    input_date = datetime.strptime(input_date, '%d-%m-%Y')
    age = today.year - input_date.year
    if input_date.month > (today.month):
        age -= 1
    elif input_date.month == today.month and input_date.day > today.day:
        age -=1
    return age 

print(age(input("Date: ")))