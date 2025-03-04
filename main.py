from wheel.wheel_name import get_names
from gradeCalculator import grade_calculator as gc

fts_dict = {
    1: "Grade Calculator",
    2: "Name Wheel",
    3: "Burguer Shop",
    4: "N/A",
    5: "Leave the program"
}


def grade_calculator():
    max_p = gc.max_points()
    round_opt = gc.round_option()
    grades = gc.calculate_grades(max_p, round_opt)
    gc.print_grade(max_p, grades)


def get_choice():
    options = [1, 2, 3, 4, 5]
    while True:
        try:    
            chosen = int(input(f"\nChoose one of the following:\n(1) {fts_dict[1]}.\n(2) {fts_dict[2]}.\n(3) {fts_dict[3]}.\n(4) {fts_dict[4]}.\n(5) {fts_dict[5]}. \nInsert here: "))
            if chosen in options:
                return chosen
        except:
            print("\nPlease insert one of the numbers above.")


def redo_option_f():
    while True:
            try:
                redo_option = str(input("\nWould you like to try another function? (y/n)\nInsert here: "))
                if redo_option in ["y", "n"]:
                    return redo_option
            except:
                print("\nPlease choose yes (y) or no (n).")


def main():

    choice = get_choice()
    redo_option = None

    if choice == 1: #grade_calculator
        grade_calculator()
        redo_option = redo_option_f()

    elif choice == 2:
        get_names()

    if redo_option == "y":
        main() #re-do loop
    else:
        print("\nThank you for using our service. :)")
        return None


if __name__ == "__main__":
    main()