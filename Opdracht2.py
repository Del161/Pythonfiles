import sys

placeholder_filename = "./5uak.pdb"
atoms_dict = {
    "C" : 12.01,
    "N" : 14.01,
    "O" : 16.00,
    "S" : 32.06
}
amino_acids_dict = {
     'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M',
     "UNK" : "*"
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
        total_weight = round(total_weight + atoms_dict[atoms])
    return total_weight

def amino_acids(list_lines):
    #pre defined variables whoo
    amino_acid_string = ""
    aminoacids_end = ""

    #make a string of the aminoacids
    for lines in list_lines:
        if lines.startswith("SEQRES"):
            amino_acids_list = lines[19:71].split()
            for aminoacids in amino_acids_list:
                amino_acid_string += amino_acids_dict[aminoacids]

    #devide aminoacids in lines of 70
    for devided_item in range(0, len(amino_acid_string), 70):
        aminoacids_end += "".join(amino_acid_string[devided_item: devided_item + 70])
        aminoacids_end += "\n"
    return(aminoacids_end)

def write_results(output_name, total_weight, aminoacids_end) -> None:
    #create given output filename
    with open(output_name, "w") as writefile:
        # loop items and write it to the file
        writefile.write("The Weight is around: ")
        writefile.write(str(total_weight))
        writefile.write("\n \n")
        writefile.write(aminoacids_end)

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
    if len(arguments) < 3:
        raise Exception("No output name given")
    else:
        # get the argument and set the variable
        output_name = arguments[2]
    
    list_lines = open_file(input_name)
    total_weight = calculate_weight(list_lines)
    aminoacids_end = amino_acids(list_lines)
    write_results(output_name, total_weight, aminoacids_end)

if __name__ == "__main__":
    main()
