from wheel.wheel_name import get_names
from gradeCalculator import grade_calculator as gc
from burgerShop.main import start

fts_dict = {
    1: "Grade Calculator",
    2: "Name Wheel",
    3: "Burger Shop (GUI app)",
    4: "Leave the program"
}

def grade_calculator():
    max_p = gc.max_points()
    round_opt = gc.round_option()
    grades = gc.calculate_grades(max_p, round_opt)
    gc.print_grade(max_p, grades)

def get_choice():
    options = [1, 2, 3, 4]
    while True:
        try:
            chosen = int(input(f"\nChoose one of the following:\n(1) {fts_dict[1]}.\n(2) {fts_dict[2]}.\n(3) {fts_dict[3]}.\n(4) {fts_dict[4]}.\nInsert here: "))
            if chosen in options:
                return chosen
        except:
            print("\nPlease insert one of the numbers above.")

def redo_option_f():
    while True:
        try:
            redo_option = str(input("\nWould you like to try another function?\nYes (y)\nNo (n)\nRedo the same (s)\n\nInsert here: "))
            if redo_option in ["y", "n", "s"]:
                return redo_option
        except:
            print("\nPlease choose yes (y) or no (n).")
            

def main(same_option=None):
    if same_option == None:
        choice = get_choice()
    else:
        choice = same_option

    if choice == 1:  # grade_calculator
        grade_calculator()
        redo_option = redo_option_f()

    elif choice == 2:
        get_names()
        redo_option = redo_option_f()

    elif choice == 3:
        start()
        redo_option = redo_option_f()

    elif choice == 4:
        print("\nThank you for using our service. :)")
        return None

    if redo_option == "y":
        main()  # re-do loop
    elif redo_option == "s":
        main(choice)
    else:
        print("\nThank you for using our service. :)")
        return None

if __name__ == "__main__":
    main()
