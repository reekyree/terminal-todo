# TODO
# Open a .txt file to add tasks to
# Add and save tasks to the list
# Let the user bring up the list

def intro():
    
    # Function to display menu
    print("Hello! Please select an option")
    print("(1) Make a new list")
    print("(2) View an existing list")



def user_action():
    answer = int(input("What would you like to do? "))

    return answer



def make_list():

    todo_list = []

    task = input(("Add an item to the list: "))
    
    todo_list.append(task)


def main():
    
    # Play the intro message
    intro()

    # Get user input to decide action
    choice = user_action()
    
    # Compare user selection to start action
    if choice == 1:
        make_list()
    elif choice == 2:
        print("Not available")
    elif choice == 3:
        print("Thank you!")

if __name__ == '__main__':
    main()
