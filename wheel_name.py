import os
import json
from random import randrange

#testing json for the first time

#os.path.join gets the path

LISTS_DIR = "lists"
INDEX_FILE = os.path.join(LISTS_DIR, "#index.json")


os.makedirs(LISTS_DIR, exist_ok=True)


def save_list(my_list, list_name):
    filename = list_name + ".json"
    file_path = os.path.join(LISTS_DIR, filename) 

    with open(file_path, "w") as path_to_file:
        json.dump(my_list, path_to_file) #dump() is to save the file, requires what needs to be saved and, in this case, the path to the file since its a diff folder, otherwise we can insert just the file name

    update_index(filename)
    print(f"\nYour list will be saved as {list_name}.")


def update_index(filename):
    '''Saves a new list into the .json file'''
    
    index = load_index() #loads a copy of index.json in the lists folder as a var 
    index[filename] = os.path.join(LISTS_DIR, filename) #gets path to the new file on the copy

    with open(INDEX_FILE, "w") as filepath: #opens the path to the index.json file
        json.dump(index, filepath, indent=4) # saves the updated index dictionary to index.json permanently


def load_index():
    '''Loads the index file containing all list filenames for editing purposes.'''

    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r") as file:
            return json.load(file)
    return {}


def delete_list(filename):
        
    file_path = os.path.join(LISTS_DIR, filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        n = filename.replace(".json", "")
        print(f"Deleted '{n}' list.")

        index = load_index()
        index.pop(filename, None)

        with open(INDEX_FILE, "w") as filepath:
            json.dump(index, filepath, indent=4)
    else:
        print("List not found!")


def print_saved_files():
    index = load_index()
    
    if not index:
        print("No saved lists.")
    else:
        print("\nSaved lists:")
        for name in index.keys():
            n = name.replace(".json", "")
            print(f" - {n}")


def print_file(filename):
    file_path = os.path.join(LISTS_DIR, filename)

    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file) 
            print(data)
    except:
        print("File not found.")


def edit_list_name(file_to_edit, new_list_name):
    try:
        old_file_path = os.path.join(LISTS_DIR, file_to_edit)
        new_path_name = os.path.join(LISTS_DIR, new_list_name)
        os.rename(old_file_path, new_path_name)
        print(f"\nThe file name of {file_to_edit} was changed to {new_list_name}!")
        update_index(new_list_name) # it adds the file to the index.json

        index = load_index()
        index.pop(file_to_edit, None)

        with open(INDEX_FILE, "w") as file:
            json.dump(index, file, indent=4)
    except:
        print("\n\nAn error happened while trying to edit the file name.\n")


def spin_the_wheel(list):
    try:
        list_n = list + ".json"
        file_path = os.path.join(LISTS_DIR, list_n)

        with open(file_path, "r") as file:
            data = json.load(file)

        keep_or_remove = int(input("\nInsert (1) to keep the names while spinning or (2) to pop them out.\n\nInsert here: "))

        if keep_or_remove in [1, 2]:
            if keep_or_remove == 1:
                range = len(data)
                keep_spinning = True
                while keep_spinning:
                    random_item = randrange(0, range)
                    print(f"{data[random_item]}")
                    continue_stop = str(input("\nContinue to spin (c).\nStop spinning (s).\n\nAnswer here: ")).lower().strip()
                    if continue_stop in ["c", "s"]:
                        if continue_stop == "s":
                            break

            if keep_or_remove == 2:
                data_copy = data
                keep_spinning = True
                chosen_items = []
                while keep_spinning:

                    range = len(data_copy)
                    random_item = randrange(0, range)

                    if len(chosen_items) > 0:
                        print("\nRemoved items: ")
                        for i in chosen_items:
                            print(i)
                    print(f"\n\nChosen name: {data_copy[random_item]}")
                    chosen_items.append(data_copy[random_item])
                    data_copy.pop(random_item)

                    print(f"\nRemaining items ({range - 1}): ")
                    for i in data_copy:
                        print(i)
                    print()
                    continue_stop = str(input("\n\nContinue to spin (c).\nStop spinning (s).\n\nAnswer here: ")).lower().strip()
                    if continue_stop in ["c", "s"]:
                        if continue_stop == "s":
                            break
                    if len(data_copy) <= 0:
                        break
    except:
        print("\nAn error popped up while spinning the wheel.\n")


def newListName(name_amount, list_name):
    names_counter = 0
    names_list = []
    for _ in range(name_amount):
        amount_left = name_amount - names_counter
        print(f"Spots left: {amount_left}")
        new_name = str(input("Insert the name here: "))
        names_list.append(new_name.strip())
        names_counter += 1
    save_list(names_list, list_name)
    get_names()


def get_names():

    while True:
        try:
            new_list = int(input("\nWhat action do you wish to take?\n\n(1) New/edit list.\n(2) Spin existing list.\n(3) Check existing lists.\n(4) Delete a list. \n(5) Read a list. \n(6) Edit a list name. \n(7) Exit the program.\n\nInsert here: "))
            if new_list in [1, 2, 3, 4, 5, 6, 7]:
                if new_list == 7:
                    return
                break
        except:
            print("\nPlease insert a valid number from 1 - 7.") 

    if new_list == 1: #new list/overwrite
        while True:
            try:
                name_amount = int(input("\nInsert the pretended amount of names you are going to list: "))
                if isinstance(name_amount, int):
                    break
            except:
                print("\nInsert a valid number for the amount of names.")

        while True:
                try:
                    print_saved_files()
                    list_name = str(input('\nInsert here your list name or the name from the list you wish to edit or "exit" to leave this section: '))
                    if list_name.lower() == "exit":
                        get_names()
                        break
                    overwrite_test = list_name + ".json"
                    list_path = os.path.join(LISTS_DIR, overwrite_test)
                    if os.path.exists(list_path):
                        overwrite_opt = str(input(f'\nA list named "{list_name}" already exists. Do you wish to overwrite the list? (yes)/(no)\nAnswer here: ')).strip().lower()
                        if overwrite_opt == "no":
                            continue
                        elif overwrite_opt == "yes":
                            print(f"\nThe program will run {name_amount} times. Please, insert a singular name and click Enter. A counter will be displayed to show how many spots are left.")
                            newListName(name_amount, list_name)
                            break
                        else:
                            print('Answer "yes" or "no".')
                    else:
                        newListName(name_amount, list_name)
                        break
                except:
                    print("\nAn error occurred while creating/overwriting a list.")

    elif new_list == 2: #spin an existing list
        while True:
            try:
                print_saved_files()
                list_to_spin = input('\nChoose a list from the list above to spin the names or "exit" to leave the spin.\n\nInsert here: ')
                if list_to_spin.lower() == "exit":
                    get_names()
                    break

                spin_list_name = list_to_spin + ".json"
                list_to_spin_path = os.path.join(LISTS_DIR, spin_list_name)
 
                if os.path.exists(list_to_spin_path):
                    spin_the_wheel(list_to_spin)
                else:
                    print("\nThe list inserted does not exist.")
            except:
                print("An error showed up while starting up the wheel.")

    elif new_list == 3: #see all files
        print_saved_files()

    elif new_list == 4: #delete a list
        while True:
            try:   
                print_saved_files()
                list_t_delet = input('\nPlease insert the name of the list you wish to delete or "exit" to go out of the deleting mode.\n\nInsert here: ')
                if list_t_delet.lower() == "exit":
                    get_names()
                    break

                list_td = list_t_delet + ".json"
                list_path = os.path.join(LISTS_DIR, list_td)

                if os.path.exists(list_path):
                    delete_list(list_td)
                else:
                    print("\nThe list inserted does not exist.")
            except:
                print("\nAn error occured while trying to choose a list to delete. Try again.")

    elif new_list == 5: #read list content
        while True:
            try:
                print_saved_files()
                user_input = input('\nPlease insert the name of the list you wish to read or "exit" to go out of the deleting mode.\n\nInsert here: ')
                if user_input.lower() == "exit":
                    get_names()
                    break

                list_t_read = user_input + ".json" 
                print_file(list_t_read)

            except:
                print("\nAn error occurred while trying to read a file. Try again.")

    elif new_list == 6:
        while True:
            try:
                print_saved_files()
                list_name_input = input('\nPlease insert the name of the list you wish to edit the name or "exit" to go out of the deleting mode.\n\nInsert here: ')
                if list_name_input.lower() == "exit":
                    get_names()
                    break

                list_to_edit = list_name_input + ".json"
                path_test = os.path.join(LISTS_DIR, list_to_edit)

                if os.path.exists(path_test):
                    new_list_name = input('\nPlease insert the new name of the selected list.\n\nInsert here: ')
                    new_list_name_c = new_list_name + ".json"
                    edit_list_name(list_to_edit, new_list_name_c)
                else:
                    print("\nList not found.")
            except:
                print("\nChosen file not found. Try again.")


def main():
    get_names()


if __name__ == "__main__":
    main()