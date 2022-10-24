import sys

#how to use
# use commandline arguments in this fashion
# replace inputname with the pdb files name, and inputname1 with the fasta filename
# python3 script2_2.py inputname.pdb inputname2.fasta outputname.txt
# file made on python version 3.10.7

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
     'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M',
     "UNK" : "*"
     }

amino_acids_weight_dict = {
"A"	: 89.1,  "R" : 174.2, "N" : 132.1,
"D"	: 133.1, "C" : 121.2, "E" : 147.1,
"Q"	: 146.2, "G" : 75.1,  "H" : 155.2, 
"I"	: 131.2, "L" : 131.2, "K" : 146.2,
"M"	: 149.2, "F" : 165.2, "P" : 115.1,
"S"	: 105.1, "T" : 119.1, "W" : 204.2,
"Y"	: 181.2, "V" : 117.1, "*" : 110
#unkown aminoacid gets the avarage weight of an aminoacid which is 110
}

hydro_dict = {
"I" :	4.5, "V" :	4.2, "L" :	3.8,
"F" :	2.8, "C" :	2.5, "M" :	1.9,
"A" :	1.8, "G" :	-0.4, "T" :	-0.7,
"S" :	-0.8, "W" : -0.9, "Y" :	-1.3,
"P" :	-1.6, "H" :	-3.2, "E" :	-3.5,
"Q" :	-3.5, "D" :	-3.5, "N" :	-3.5,
"K" :	-3.9, "R" :	-4.5, "*" :   -0.49 
# * is average of all aminoacids
}

def open_file(input_name, comparison_name):
        # read pdb file
    with open(input_name, "r") as file:
        # set file lines to variable
        list_lines = list(file.readlines())

    #read comparison fasta file
    with open(comparison_name, "r") as file2:
        # set file lines to variable
        comparison_lines = list(file2.readlines())
    return list_lines, comparison_lines

def calculate_weight(list_lines):
    #calculates the atoms weight
    atoms_list = []
    total_weight = 0 

    for lines in list_lines:
        if lines.startswith("ATOM"):
            atoms_list.append(lines[77:78])
    for atoms in atoms_list:
        total_weight = round(total_weight + atoms_dict[atoms], 2)
    return total_weight

#retrieves helix and sheet aminoacids from file
def get_helix_sheet_strings(amino_acid_string, list_lines):
    #more predefined vars
    helix_residue_start = ""
    helix_residue_end = ""
    helix_sequence = ""
    #retrieve helix information
    for lines in list_lines:
        if lines.startswith("HELIX"):
            helix_residue_start = lines[22:25].split()
            helix_residue_end = lines[34:37].split()
            helix_amino_acids = amino_acid_string[int(helix_residue_start[0]): int(helix_residue_end[0])]
            helix_sequence += helix_amino_acids

    #more predefined vars
    sheet_residue_start = ""
    sheet_residue_end = ""
    sheet_sequence = ""
    #retrieve sheet information
    for lines in list_lines:
        if lines.startswith("SHEET"):
            sheet_residue_start = lines[23:26].split()
            sheet_residue_end = lines[34:37].split()
            sheet_amino_acids = amino_acid_string[int(sheet_residue_start[0]): int(sheet_residue_end[0])]
            sheet_sequence += sheet_amino_acids
    return helix_sequence, sheet_sequence

#retrieves all aminoacids from the file
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

    #devide aminoacids in solid lines of 70
    for devided_item in range(0, len(amino_acid_string), 70):
        aminoacids_end += "".join(amino_acid_string[devided_item: devided_item + 70])
        aminoacids_end += "\n"
    return aminoacids_end, amino_acid_string 

#calculates aminoacid weight
def calculate_aminoacid_weight(amino_acid_string):
    #pre define vars
    aminoacid_weight = 0
    weight_loss = (len(amino_acid_string) - 2) * 18.01
    #use the letters in the aminoacid string as a key for the dict with weights.
    for letter in amino_acid_string:
        aminoacid_weight = round(aminoacid_weight + amino_acids_weight_dict[letter])
    #remove the water weight
    aminoacid_weight = aminoacid_weight - weight_loss
    return aminoacid_weight

def compare_files(comparison_lines, aminoacids_end):
    #predefined variaaableees
    comparison_list = []
    aminoacids_list = []
    endresult_compared_list = ""
    comparison_string = ""
    rownumber1 = 0
    rownumber = 0
    checklist_amino = []
    checklist_amino_1 = []

    #remove newlines from fasta sequence, check if its not header, turn it into string to prevent issues with length
    for lines in comparison_lines:
        if not lines.startswith(">"):
            lines = lines.strip()
            comparison_string += lines

    #devide in rows of 70 for neat comparison
    for rows in range(0, len(comparison_string), 70):
        comparison_list.append("Fasta sequence line: " + str(rownumber)+ " :"+ comparison_string[rows: rows + 70])
        checklist_amino.append(comparison_string[rows: rows + 70])
        rownumber += 1

    #remove newlines from pdb sequence
    aminoacids_string = aminoacids_end.replace("\n", "")

    for rows in range(0, len(aminoacids_string), 70):
        aminoacids_list.append("PDB sequence   line: " + str(rownumber1)+ " :"+ aminoacids_string[rows: rows + 70])
        checklist_amino_1.append(aminoacids_string[rows: rows + 70])
        rownumber1 += 1

    #check which list is shortest to prevent index errors
    if len(aminoacids_list) == len(comparison_list):
        length_list = len(comparison_list)       
        print("lists same length, no issues")
    elif len(aminoacids_list) > len(comparison_list):
        length_list = len(comparison_list)
        print("PDB sequence is longer, only comparing for length of shorter FASTA file")
        print("length PDB sequence: ", len(aminoacids_list), "length FASTA sequence", len(comparison_list))
    else: 
        length_list = len(aminoacids_list)
        print("FASTA sequence is longer, only comparing for length of shorter PDB file")
        print("length PDB sequence: ", len(aminoacids_list), "length FASTA sequence", len(comparison_list))

    #save the formatted lines to a list
    for linecount in range(length_list):
        endresult_compared_list += (comparison_list[linecount]+ "\n"+ aminoacids_list[linecount]+ "\n \n")
        #check if there are differences
        if not checklist_amino[linecount] == checklist_amino_1[linecount]:
            print("difference in line", linecount)

    return endresult_compared_list
    
def calculate_hydrophilicity(aminoacids_end, sheet_sequence, helix_sequence):
    #p-p-p-predefined valueees
    sheet_hydro_value = 0
    helix_hydro_value = 0
    totalamino_hydro_value = 0
    aminoacidstring = aminoacids_end.replace("\n", "")

    #calculate sheet hydrophilicity value
    for char in sheet_sequence:
        sheet_hydro_value += hydro_dict[char]

    #calculate aminoacid hydrophilicity value
    for char in aminoacidstring:
        totalamino_hydro_value += hydro_dict[char]   

    #calculate helix hydrophilicity value
    for char in helix_sequence:
        helix_hydro_value += hydro_dict[char]

    #calculate averages
    helix_hydro_value = helix_hydro_value / len(helix_sequence)
    sheet_hydro_value = sheet_hydro_value / len(sheet_sequence)
    totalamino_hydro_value = totalamino_hydro_value / len(aminoacidstring)

    #put them in a list
    hydro_results_list = [sheet_hydro_value, helix_hydro_value, totalamino_hydro_value]
    return hydro_results_list



def write_results(output_name, total_weight, aminoacid_weight, aminoacids_end, sheet_sequence, helix_sequence, endresult_compared_list, hydro_results_list ):
    #write the weight results to a file
    #create given output filename
    with open(output_name, "w") as writefile:
        # loop items and write it to the file
        writefile.write("The weight of the atoms is around: "+ str(total_weight) + "\n")
        writefile.write("The weight of the aminoacids is around: "+ str(aminoacid_weight) + "\n \n")

        #write hydrophilicity to file
        writefile.write("average hydrophilicity of aminoacid sequence is: " + str(hydro_results_list[2]) + "\n")
        writefile.write("average hydrophilicity of helix sequence is: " + str(hydro_results_list[1]) + "\n")
        writefile.write("average hydrophilicity of sheet sequence is: " + str(hydro_results_list[0]) + "\n \n")

        #write the various sequences to file
        writefile.write("The aminoacid sequence: \n")
        writefile.write(aminoacids_end + "\n \n")
        writefile.write("The helix sequence: \n")
        writefile.write(helix_sequence + "\n \n")
        writefile.write("The sheet sequence: \n")
        writefile.write(sheet_sequence + "\n \n")

        #write the compared files to file to compare them easily
        writefile.write("the files compared below eachother: \n")
        writefile.write(endresult_compared_list)



def main():
    # get the given arguments
    arguments = sys.argv
    # pre defined variables
    input_name = ""
    output_name = ""
    comparison_name = ""

    if len(arguments) < 2:
        raise Exception("No input filename given, please use commandline arguments. (python3 script2_2.py PDB file inputname, Fasta inputname, output filename )")
    else:
        # get the argument and set the variable
        input_name = arguments[1]
    
    # check if it has the comparison file argument
    if len(arguments) < 3:
        raise Exception("No comparison filename given")
    else:
        # get the argument and set the variable
        comparison_name = arguments[2]

    # check if it has the file output argument
    if len(arguments) < 4:
        raise Exception("No output filename given")
    else:
        # get the argument and set the variable
        output_name = arguments[3]
    
    list_lines, comparison_lines = open_file(input_name, comparison_name)
    total_weight = calculate_weight(list_lines)
    aminoacids_end, amino_acid_string  = amino_acids(list_lines)
    aminoacid_weight = calculate_aminoacid_weight(amino_acid_string)
    helix_sequence, sheet_sequence = get_helix_sheet_strings(amino_acid_string, list_lines)
    endresult_compared_list = compare_files(comparison_lines, aminoacids_end)
    hydro_results_list = calculate_hydrophilicity(aminoacids_end, sheet_sequence, helix_sequence)
    write_results(output_name, total_weight, aminoacid_weight, aminoacids_end, sheet_sequence, helix_sequence, endresult_compared_list, hydro_results_list)
    print("information and results were logged in ", output_name)

if __name__ == "__main__":
    main()
