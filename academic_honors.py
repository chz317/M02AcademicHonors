"""
Joseph Cheesebourough
academic_honors.py
This app accepts student names and GPAs, checks if they qualify for the Dean's List or the Honor Roll,
and processes records until the last name 'ZZZ' is entered. The app then outputs the qualification results.
"""

def main():
    while True:
        # Ask for student's last name
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if last_name.upper() == 'ZZZ':
            break

        # Ask for student's first name
        first_name = input("Enter the student's first name: ")

        # Ask for student's GPA as float
        while True:
            gpa_input = input("Enter the student's GPA: ")
            if gpa_input.replace('.', '', 1).isdigit() and gpa_input.count('.') <= 1:
                gpa = float(gpa_input)
                break
            else:
                print("Invalid input for GPA. Please enter a numeric value.")

        # Test if the student's GPA is 3.5 or greater and print message for the Dean's List
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        
        # Test if the student's GPA is 3.25 or greater and print message for the Honor Roll
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} has not qualified for the Dean's List or the Honor Roll.")

if __name__ == "__main__":
    main()