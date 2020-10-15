import sys

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
        line_list.append(line)

    for item in line_list:
        values = item.split(",")
        address_dict[values[0]] = (values[1], values[2], values[3], 
                                  values[4], values[5].strip())

    return address_dict

address_file = input_file()

print(address_file)



