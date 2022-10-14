import sys

placeholder_filename = "./5uak.pdb"
atoms_dict = {
    "C" : 12,
    "N" : 14,
    "O" : 16,
    "S" : 32
}

def open_file(input_name):
        # read pdb file
    with open(input_name, "r") as file:
        # set file lines to variable
        list_lines = list(file.readlines())
    return list_lines

def calculate_weight(list_lines):
    #bereken het gewicht van de atomen 
    atoms_list = []
    total_weight = 0 

    for lines in list_lines:
        if lines.startswith("ATOM"):
            atoms_list.append(lines[77:78])
    for atoms in atoms_list:
        total_weight = total_weight + atoms_dict[atoms]
    print(total_weight)

def main() -> None:
    # get the given arguments
    arguments = sys.argv
    # pre devine variables
    input_name = ""
    output_name = ""

    if len(arguments) < 2:
        raise Exception("No input name given")
    else:
        # get the argument and set the variable
        input_name = arguments[1]

    # check if it has the file output argument
    #if len(arguments) < 3:
    #    raise Exception("No output name given")
    #else:
    #    # get the argument and set the variable
    #    output_name = arguments[2]
    
    list_lines = open_file(input_name)
    calculate_weight(list_lines)

if __name__ == "__main__":
    main()
