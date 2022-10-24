import sys


def open_file(input_name, comparison_name):
        # reads input file
    with open(input_name, "r") as file:
        # set file lines to variable
        file_content = list(file.readlines())
    return file_content


def extract_file_data(file_content):
    #predefined variableee
    extracted_data = ""
    line_index = 0
    mrna_location = 0
    mRNA_info = []
    clean_content = []
    positions = ""
    mrna_start_end = []

    #remove all newlines \n
    for lines in file_content:
        clean_content.append(lines.strip())

    #find the startpos of the mrna line, and append all the lines that include information
    for lines in clean_content:
        if lines.startswith("mRNA"):
           mrna_location = line_index
           for lines in clean_content[line_index: len(file_content)]:
                if lines.startswith("/"):
                    break
                else:
                    mRNA_info.append(lines) 
        else: line_index += 1
    line_index = 0

    #remove all special symbols, and split in the place between numbers.
    positions = "".join(mRNA_info)
    positions = positions.replace(",","..").replace("<","..").replace(">","").split("..")
    positions.pop(0)

    #append in pairs of 2(start and end position)
    for place in range(0, len(positions), 2):
        mrna_start_end.append(positions[place: place + 2])
    
    for lines in mrna_start_end:
        print(lines[0])
    for lines in mrna_start_end:
        print(lines[1])
    
    return extracted_data


def write_results(extracted_data, output_name):
    #write results to file
    #create given output filename
    with open(output_name, "w") as writefile:
        # write results to the file
        writefile.write("test")


def main():
   # get the given arguments
    arguments = sys.argv
    # pre defined variables
    input_name = ""
    output_name = ""

    if len(arguments) < 2:
        raise Exception("No input filename given, please use commandline arguments. (python3 script2_3.py file inputname, output filename )")
    else:
        # get the argument and set the variable
        input_name = arguments[1]
    
    # check if it has the outputname given
    if len(arguments) < 3:
        raise Exception("No output filename given")
    else:
        # get the argument and set the outputname
        output_name = arguments[2]

    file_content = open_file(input_name, output_name)
    extracted_data = extract_file_data(file_content)
    write_results(extracted_data, output_name)

if __name__ == "__main__":
    main()