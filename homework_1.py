from datetime import datetime

date_input=input('Введіть дату у форматі "РРРР-ММ-ДД" ')

def get_days_from_today(date):
    try:
        date1 = datetime.strptime(date, "%Y-%m-%d").date()
        result = date1 - datetime.today().date()
        return result.days
    except ValueError:
        date1 = datetime.strptime(date, "%Y.%m.%d").date()
        result = date1 - datetime.today().date()
        return result.days
print(get_days_from_today(date_input))