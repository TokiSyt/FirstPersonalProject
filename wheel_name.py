import os
import json

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
    print(f"\nYour file will be saved as {filename}.")


def update_index(filename):
    '''Saves a new list into the .json file'''
    
    index = load_index() #loads index.json in the lists folder 
    index[filename] = os.path.join(LISTS_DIR, filename) #gets path to the new file

    with open(INDEX_FILE, "w") as file: #opens the path to the index.json file
        json.dump(index, file, indent=4) # saves the updated index dictionary to index.json permanently


def load_index():
    '''Loads the index file containing all list filenames for editing purposes.'''

    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r") as file:
            return json.load(file)
    return {}


def load_list(filename):
    '''Loads and returns the list from the selected filename'''

    file_path = os.path.join(LISTS_DIR, filename)
    
    if not os.path.exists(file_path):
        print("File not found!")
        return None
    
    else:
        with open(file_path, "r") as file:
            return json.load(file)


def delete_list(filename):
        
    file_path = os.path.join(LISTS_DIR, filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted '{filename}'.")

        index = load_index()
        index.pop(filename, None)

        with open(INDEX_FILE, "w") as file:
            json.dump(index, file, indent=4)
    else:
        print("File not found!")


def print_saved_files():
    index = load_index()
    if not index:
        print("No saved lists.")
    else:
        print("\nSaved lists:")
        for name in index.keys():
            print(f" - {name}")


def print_file(filename):
    file_path = os.path.join(LISTS_DIR, filename)
    try:
        with open(file_path, "r") as file:
            data = json.load(file) 
        print(data)
    except:
        print("File not found.")

def print_file(filename):
    file_path = os.path.join(LISTS_DIR, filename)
    try:
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
    except:
        print("\n\nAn error happened while trying to edit the file name.\n")
    #good example of what could be an anonym func in Go xd lol


def spin_the_wheel(list):
    pass


def get_names():

    while_breaker = True

    while while_breaker:
        try:
            new_list = int(input("\nWhat action do you wish to take?\n\n(1) New/edit list.\n(2) Spin existing list.\n(3) Check existing lists.\n(4) Delete a list. \n(5) Read a list. \n(6) Edit a list name. \n(7) Exit the program.\n\nInsert here: "))
            if new_list in [1, 2, 3, 4, 5, 6, 7]:
                if new_list == 7:
                    return None
                else:
                    break
        except:
            print("Please insert a valid number from 1 - 5.") 

    while_breaker = True
    while while_breaker:
        try:
            if new_list in [1]:
                name_amount = int(input("\nInsert the pretended amount of names you are going to list: "))
                if isinstance(name_amount, int):
                    while_breaker = False
            else:
                while_breaker = False
        except:
            print("\nInsert a valid number for the amount of names.")

    names_counter = 0
    names_list = []
    while_breaker = True
    while while_breaker:
        try:
            if new_list in [1]:
                print_saved_files()
                list_name = str(input("\nPlease insert here your list name or the name from the list you wish to edit: "))
                overwrite_test = list_name + ".json"
                list_path = os.path.join(LISTS_DIR, overwrite_test)
                if os.path.exists(list_path):
                    overwrite_opt = str(input(f'\nA list named "{list_name}" already exists. Do you wish to overwrite the list?\nAnswer here: ')).strip().lower()
                    if overwrite_opt == "no":
                        get_names()
                        while_breaker = False
                        break
                    elif overwrite_opt == "yes":
                        print(f"\nThe program will run {name_amount} times. Please, insert a singular name and click Enter. A counter will be displayed to show how many spots are left.")
                        for _ in range(name_amount):
                            amount_left = name_amount - names_counter
                            print(f"Spots left: {amount_left}")
                            new_name = str(input("Insert the name here: "))
                            names_list.append(new_name.strip())
                            names_counter += 1
                        save_list(names_list, list_name)
                        get_names()
                        while_breaker = False
                    else:
                        a = 0 / 2 #error trigger
            else:
                while_breaker = False

        except:
            print("\nPlease follow all instructions")
    while_breaker = True

    if new_list == 2: #spin an existing list
        #spin_the_wheel(list)
        pass

    if new_list == 3: #see all files
        print_saved_files()
        get_names()

    while while_breaker:
        try:
                
            if new_list == 4: #delete a list
                print_saved_files()
                list_t_delet = input('\nPlease insert the name of the list you wish to delete or "exit" to go out of the deleting mode.\n\nInsert here: ')
                if list_t_delet == "exit":
                    while_breaker = False
                    get_names()
                    break
                list_path = os.path.join(LISTS_DIR, list_t_delet)
                if os.path.exists(list_path):
                    delete_list(list_t_delet)
            else:
                while_breaker = False
        except:
            print("\nAn error occured while trying to choose a list to delete. Try again.")
    while_breaker = True

    while while_breaker:
        try:
            if new_list == 5: #read list content
                print_saved_files()
                list_t_read = input('\nPlease insert the name of the list you wish to read or "exit" to go out of the deleting mode.\n\nInsert here: ')
                if list_t_read == "exit":
                    while_breaker = False
                    get_names()
                    break
                print_file(list_t_read)
                get_names()
                while_breaker = False
            else:
                while_breaker = False
        except:
            print("\nAn error occurred while trying to read a file. Try again.")
    while_breaker = True


    while while_breaker:
        if new_list == 6:
            list_name_t_edit = input('\nPlease insert the name of the list you wish to edit the name or "exit" to go out of the deleting mode.\n\nInsert here: ')
            if list_name_t_edit == "exit":
                while_breaker = False
                get_names()
                break
            new_list_name = input('\nPlease insert the new name of the selected list.\n\nInsert here: ')
            edit_list_name(list_name_t_edit, new_list_name)
        else:
            while_breaker = False
    while_breaker = True


def main():
    get_names()


if __name__ == "__main__":
    main()