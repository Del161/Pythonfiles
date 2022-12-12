"""
Author: Delshad Vegter
date: 6-12-22
"""
import sys  # for commandline arguments

def help():
    print("xdata_extractor is a function that takes a filename, and uses it to make a dictionary"
          "using the first word as a key, and the rest of the values as a list")

def open_file(filename):
    """
    turns the file into a list
    :param filename:
    :return: a list of strings
    """

    # predefined variables
    file_content = []

    with open("./" + filename, "r") as file:
        # set file lines to variable
        file_content = list(file.readlines())
    return file_content

def extract_data_values(file_content):
    """
    Extracts data values from a list of a .csv file
    :return:
    """

    file_dict = {}
    for lines in file_content[1:]:
        lines = lines.strip().split(",")
        identifier = lines.pop(0)
        file_dict[identifier] = lines
    return file_dict

def xdata_extractor(filename):
    file_content = open_file(filename)
    file_dict = extract_data_values(file_content)
    header = extract_header(file_content)
    file_content_header = (file_dict, header)
    return file_content_header

def extract_header(file_content):
    """
    extracts the header from a csv file
    :return:
    """
    header = file_content[0]
    header = header.strip().split(",")
    return header

def main():
    arguments = sys.argv
    filename = arguments[1]
    xdata_extractor(filename)

# to protect against problems when imported
if __name__ == "__main__":
    main()
