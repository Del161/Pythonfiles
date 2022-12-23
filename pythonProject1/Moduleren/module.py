"""
Graph creator program
commandline arguments order: python3 module.py filename.csv wanted_graph ylabel,xlabel,title
Wanted graph can be: "bar_chart", "boxplot"
ylabel xlabel and title can be replaced with an * to be left empty
Author: Delshad Vegter
Date:6-12-22
"""

import csvreader as csv
from graphcreator import barchart, boxplot
import sys

def main():
    """
    Where all functions are run in order
    """
    # predefined variables
    user_labels = []

    # assign the commandline arguments, and check if there are enough
    arguments = sys.argv
    if len(arguments) > 1:
        filename = arguments[1]
    else:
        raise Exception("too few arguments given")

    if len(arguments) > 3: user_labels = arguments[3]

    # extract the header and values from the csv file
    file_values_header = csv.xdata_extractor(filename)
    if arguments[2] == "barchart":
        barchart(file_values_header, user_labels)
    elif arguments[2] == "boxplot":
        boxplot(file_values_header, user_labels)

# to protect against problems if imported
if __name__ == "__main__":
    main()