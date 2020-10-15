import sys

def main():
    # Call the input_file function to read file.
    file_dictionary = input_file()
    # Main input loop.
    while True:
        choice = input("Lookup (1) phone numbers or (2) addresses: ")
        name = input("Enter space-separated first and last name: ")
        name = name.lower()
        # Call the display_output file to show chosen output.
        display_ouput(file_dictionary, name, choice)
        # End program if user enters blank line
        if choice == "" or name == "":
            break

def input_file():
    """Read addresses from a file into a dictionary."""
    line_list = []
    address_dict = {}

    try:
        f = open("address.txt", 'r')
    except FileNotFoundError:
        print("error: must use a valid filename.")
        sys.exit(1)

    while True:
        line = f.readline()
        if line == "":
            break
        line_list.append(line.lower())

    for item in line_list:
        values = item.split(",")
        address_dict[values[0]] = (values[1], values[2], values[3], 
                                  values[4], values[5].strip())

    f.close()
    return address_dict

#address_file = input_file()

#print(address_file)

def display_ouput(addresses, input_name, user_choice=1):
    """Format output to display phone number or address."""
    # Check to see if entered name is in dictionary, if yes, proceed.
    if input_name in addresses:
        # Separate dictionary entry into specific one for inputted name.
        entry = addresses[input_name]
        # Use user_choice arguement to determine which output option to display
        if user_choice == '1':
            print("Phone:\t\t" + entry[4])
        elif user_choice == '2':
            print("Street:\t\t" + entry[0].title())
            print("City:\t\t" + entry[1].title())
            print("State:\t\t" + entry[2].upper())
            print("Zip Code:\t" + entry[3].title())
    # If entered name is not in dictionary, prompt user to try again.
    else:
        print("Name not found. Please try again")

if __name__ == "__main__":
    main()




