value_error_m = "\nPlease, enter a valid number.\n"


def max_points():
    while True:
        try:
            return float(input("What is your test max points?\nAnswer here: "))
        except ValueError:
            print(value_error_m)


def round_option():
    while True:
        try:
            option = int(input('''
    Please, type one (1) for round grades or two (2) for decimal grades.
    
    Insert here: '''))
            
            if option in [1, 2]:
                return option
            else:
                print("\nPlease, choose a number between 1 and 2.")
        except ValueError:
            print(value_error_m)


def calculate_grades(max_points, option):
    grades = [max_points * x for x in [0.90, 0.89, 0.75, 0.74, 0.50, 0.49, 0.35, 0.34]]
    grades = [round(grade) for grade in grades]

    for grade_i in range(len(grades)):
        if grades[grade_i] is not grades[-1] and grades[grade_i] == grades[grade_i + 1]:
            grades[grade_i] += 1 if option == 1 else 0.5

    return grades


def print_grade(max_points, formatted_grades):

    print(f'''
    Your grades should be:
       1 - {int(max_points)} - {formatted_grades[0]}
       2 - {formatted_grades[1]} - {formatted_grades[2]}
       3 - {formatted_grades[3]} - {formatted_grades[4]}
       4 - {formatted_grades[5]} - {formatted_grades[6]}
       5 - {formatted_grades[7]} - 0
    ''')