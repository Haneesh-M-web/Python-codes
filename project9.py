print("NAME:Haneesh M")
print("USN:1AY24AI038")
print("SECTION:M")
from datetime import datetime, timedelta

def show_day_of_week():
    today = datetime.today()
    print("Today is:", today.strftime("%A"))

def birthday_info():
    bday = input("Enter your birthday (YYYY-MM-DD): ")
    bday = datetime.strptime(bday, "%Y-%m-%d")
    now = datetime.now()
    age = now.year - bday.year - ((now.month, now.day) < (bday.month, bday.day))
    next_bday = bday.replace(year=now.year)
    if next_bday < now:
        next_bday = next_bday.replace(year=now.year + 1)
    delta = next_bday - now
    seconds = int(delta.total_seconds())
    print(f"You are {age} years old.")
    print(f"Time until next birthday: {delta.days} days, {seconds//3600%24} hours, {seconds//60%60} mins, {seconds%60} secs.")

def double_day():
    b1 = datetime.strptime(input("First birthday (YYYY-MM-DD): "), "%Y-%m-%d")
    b2 = datetime.strptime(input("Second birthday (YYYY-MM-DD): "), "%Y-%m-%d")
    older, younger = sorted([b1, b2])
    double = older + 2 * (younger - older)
    print("Double Day:", double.date())

def n_times_day():
    b1 = datetime.strptime(input("First birthday (YYYY-MM-DD): "), "%Y-%m-%d")
    b2 = datetime.strptime(input("Second birthday (YYYY-MM-DD): "), "%Y-%m-%d")
    n = float(input("Enter n (e.g. 2 for double): "))
    older, younger = sorted([b1, b2])
    target = older + timedelta(seconds=(younger - older).total_seconds() / (n - 1))
    print(f"{n} times older day:", target.date())

def main():
    while True:
        print("\n1. Day of week\n2. Birthday info\n3. Double Day\n4. N-times Day\n5. Exit")
        choice = input("Choose (1-5): ")
        if choice == '1': show_day_of_week()
        elif choice == '2': birthday_info()
        elif choice == '3': double_day()
        elif choice == '4': n_times_day()
        elif choice == '5': break
        else: print("Try again.")
main()
