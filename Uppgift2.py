# uppgift2.py
# Programmering nivå 1 – Villkor & logik: Uppgift 2 (övningar 1–6 + bonus)

def ask_int(prompt, min_val=None, max_val=None):
    """Säkrare heltalsinmatning (tillåter t.ex. mellanslag, felhantering)."""
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if min_val is not None and val < min_val:
                print(f"Värdet måste vara ≥ {min_val}. Försök igen.")
                continue
            if max_val is not None and val > max_val:
                print(f"Värdet måste vara ≤ {max_val}. Försök igen.")
                continue
            return val
        except ValueError:
            print("Ogiltigt heltal, försök igen.")

def exercise_1_even_or_odd():
    n = ask_int("Enter a number: ")
    print("Even" if n % 2 == 0 else "Odd")

def exercise_2_age_categories():
    age = ask_int("Enter your age: ", min_val=0)
    if age < 13:
        print("Child")
    elif 13 <= age <= 17:
        print("Teenager")
    else:
        print("Adult")

def exercise_3_compare_two_numbers():
    a = ask_int("Enter the first number: ")
    b = ask_int("Enter the second number: ")
    if a > b:
        print("The first number is larger.")
    elif b > a:
        print("The second number is larger.")
    else:
        print("The numbers are equal.")

def exercise_4_grade_checker():
    score = ask_int("Enter your score (0–100): ", min_val=0, max_val=100)
    if 90 <= score <= 100:
        print("Grade: A")
    elif 80 <= score <= 89:
        print("Grade: B")
    elif 70 <= score <= 79:
        print("Grade: C")
    elif 60 <= score <= 69:
        print("Grade: D")
    else:
        print("Grade: F")

def exercise_5_password_checker():
    pwd = input("Enter the password: ")
    print("Access granted" if pwd == "secret123" else "Access denied")

def exercise_6_logical_operator_test():
    age = ask_int("Enter your age: ", min_val=0)
    country = input("Enter your country: ").strip().lower()
    if age >= 18 and country in ("sweden", "sverige"):
        print("You can vote in Sweden.")
    else:
        print("You can’t vote in Sweden.")

def bonus_day_of_week():
    day = input("What day is it? ").strip().lower()
    weekdays = {"monday","tuesday","wednesday","thursday","friday",
                "måndag","tisdag","onsdag","torsdag","fredag"}
    weekend  = {"saturday","sunday","lördag","söndag"}
    if day in weekdays:
        print("Time for school/work!")
    elif day in weekend:
        print("Enjoy your weekend!")
    else:
        print("That doesn’t seem like a day of the week...")

def menu():
    options = {
        "1": ("Exercise 1: Even or odd", exercise_1_even_or_odd),
        "2": ("Exercise 2: Age categories", exercise_2_age_categories),
        "3": ("Exercise 3: Compare two numbers", exercise_3_compare_two_numbers),
        "4": ("Exercise 4: Grade checker", exercise_4_grade_checker),
        "5": ("Exercise 5: Password checker", exercise_5_password_checker),
        "6": ("Exercise 6: Logical operator test", exercise_6_logical_operator_test),
        "7": ("Bonus: Day of the week", bonus_day_of_week),
        "0": ("Exit", None),
    }
    while True:
        print("\n=== Menu ===")
        for k, (title, _) in options.items():
            print(f"{k}) {title}")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Bye!")
            break
        fn = options.get(choice, (None, None))[1]
        if fn:
            print()
            fn()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
