"""
Personal Information Collector
Asks for basic info, calculates age (based on 2025) and height in meters,
then prints a formatted summary.
"""

CURRENT_YEAR = 2025

def main():
    # Collect input
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    year_of_birth = int(input("What year were you born? "))
    height_cm = float(input("What is your height in cm? "))
    country = input("What country do you live in? ")

    # Calculate
    age = CURRENT_YEAR - year_of_birth
    height_m = height_cm / 100

    # Output summary
    print("\n===== Personal Information Summary =====")
    print(f"Name: {first_name} {last_name}")
    print(f"Age: {age} years old")
    print(f"Height: {height_m:.2f} meters")
    print(f"Country: {country}")
    print("========================================")

if __name__ == "__main__":
    main()
