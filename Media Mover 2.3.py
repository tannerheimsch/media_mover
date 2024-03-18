import os
import subprocess

def clear_screen():
    # This function will not clear the screen if the error message is displayed.
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def print_ascii_art():
    print(r"""
 __    __     ______     _____     __     ______        __    __     ______     __   __   ______     ______    
/\ "-./  \   /\  ___\   /\  __-.  /\ \   /\  __ \      /\ "-./  \   /\  __ \   /\ \ / /  /\  ___\   /\  == \   
\ \ \-./\ \  \ \  __\   \ \ \/\ \ \ \ \  \ \  __ \     \ \ \-./\ \  \ \ \/\ \  \ \ \'/   \ \  __\   \ \  __<   
 \ \_\ \ \_\  \ \_____\  \ \____-  \ \_\  \ \_\ \_\     \ \_\ \ \_\  \ \_____\  \ \__|    \ \_____\  \ \_\ \_\ 
  \/_/  \/_/   \/_____/   \/____/   \/_/   \/_/\/_/      \/_/  \/_/   \/_____/   \/_/      \/_____/   \/_/ /_/ 
                                                                                                            v2.3                                                                                    
          """)

def list_subfolders(root='.', option=None):
    subfolders_map = {}
    for folder in os.listdir(root):
        if os.path.isdir(folder):
            if option == '2':
                subfolders = [file for file in os.listdir(folder) if os.path.isdir(os.path.join(folder, file)) or file.endswith(('.mp4', '.mkv'))]
            else:
                subfolders = [subfolder for subfolder in os.listdir(folder) if os.path.isdir(os.path.join(folder, subfolder))]
            if subfolders:
                subfolders_map[folder] = subfolders
    return subfolders_map

def move_subfolders(subfolders, destination, option, teracopy_path):
    destination_length = len("DESTINATION PATH: " + destination)

    print("=" * destination_length)
    print(f"DESTINATION PATH: {destination}")
    print("=" * destination_length)

    for main_folder, subfolders_list in subfolders.items():
        print(f"- {main_folder}: {', '.join(subfolders_list)}\n")
    prompt = "Enter the name of the TV show(s) you want to move (from the names above, separated by commas):\n" if option == '1' else "Enter the name of the movie(s), including the file type, that you want to move (from the names above, separated by commas):\n"
    
    while True:
        selected_subfolders = input(prompt).split(',')
        all_found = True
        for subfolder in selected_subfolders:
            found = False
            for main_folder, subfolders_list in subfolders.items():
                if subfolder.strip() in subfolders_list:
                    found = True
                    source = os.path.abspath(os.path.join(main_folder, subfolder.strip()))
                    if subfolder.endswith(('.mp4', '.mkv')):
                        folder_name = os.path.splitext(subfolder.strip())[0]
                        destination_folder = os.path.join(destination, folder_name)
                        os.makedirs(destination_folder, exist_ok=True)
                        destination = destination_folder
                    if os.path.exists(teracopy_path):
                        subprocess.run([teracopy_path, 'Move', source, destination, '/OverwriteAll', '/Close'])
                        print(f"\nMoved {subfolder} to {destination}\n")
                    else:
                        print("\nERROR: TeraCopy.exe not found, please change the .exe destination.\n")
                    break
            if not found:
                print(f"Subfolder '{subfolder.strip()}' not found.")
                all_found = False
        if all_found:
            break

def set_destination_paths():
    clear_screen()
    print_ascii_art()
    config_path = 'mm_config.txt'
    default_teracopy_path = r'C:\Program Files\TeraCopy\TeraCopy.exe'
    tv_shows_dest, movies_dest, teracopy_path = 'None', 'None', default_teracopy_path
    
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            destinations = [line.strip() for line in file.readlines()]
            if len(destinations) >= 3:
                tv_shows_dest, movies_dest, teracopy_path = destinations[:3]
    
    print("Current Media Destination Paths:")
    print(f"1. TV Shows = {tv_shows_dest}")
    print(f"2. Movies = {movies_dest}")
    print("\nTeraCopy.exe Path:")
    print(teracopy_path)

    while True:
        selection = input("\nSelect a path to change (1, 2, TC) or type '0' to go back to the main menu: ").lower()
        if selection == '1':
            new_dest = input("Enter destination path for TV Shows: ")
            tv_shows_dest = new_dest
            with open(config_path, 'w') as file:
                file.write(f"{tv_shows_dest}\n{movies_dest}\n{teracopy_path}")
            print(f"\nDestination path for TV Shows set.")
        elif selection == '2':
            new_dest = input("Enter destination path for Movies: ")
            movies_dest = new_dest
            with open(config_path, 'w') as file:
                file.write(f"{tv_shows_dest}\n{movies_dest}\n{teracopy_path}")
            print(f"\nDestination path for Movies set.")
        elif selection == 'tc':
            new_teracopy_path = input("Enter TeraCopy.exe path: ")
            teracopy_path = new_teracopy_path
            with open(config_path, 'w') as file:
                file.write(f"{tv_shows_dest}\n{movies_dest}\n{teracopy_path}")
            print(f"\nTeraCopy.exe path set.")
        elif selection == '0':
            print("")
            break  # Exit the loop and go back to the main menu
        else:
            print("Invalid selection.")

def main():
    while True:
        clear_screen()
        print_ascii_art()
        print("1 - TV Show")
        print("2 - Movie")
        print("3 - Setup Destination Folders/TeraCopy Path")
        print("0 - Exit")
        option = input("\nEnter an option: ")

        if option in ('1', '2'):
            clear_screen()
            print_ascii_art()
            subfolders = list_subfolders(option=option)
            config_path = 'mm_config.txt'
            if os.path.exists(config_path):
                with open(config_path, 'r') as file:
                    destinations = [line.strip() for line in file.readlines()]
                    destination = destinations[0] if option == '1' else destinations[1]
            else:
                print("ERROR: Destination paths are not set. Set them using Option 3.\n")
                input("Press Enter to continue...")
                continue

            if destination == 'None':
                print("ERROR: Destination path is not set. Set it using Option 3.\n")
                input("Press Enter to continue...")
                continue

            move_subfolders(subfolders, destination, option, destinations[2])
        elif option == '3':
            clear_screen()
            print_ascii_art()
            set_destination_paths()
        elif option == '0':
            clear_screen()
            print("Exiting...")
            break
        else:
            print("Invalid option.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
