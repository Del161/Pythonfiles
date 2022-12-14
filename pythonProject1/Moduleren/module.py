"""
Graph creator program
commandline arguments order: python3 module.py filename.csv wanted_graph
Wanted graph can be: "bar_chart"
Author: Delshad Vegter
Date:6-12-22
"""

import csvreader as csv
import graphcreator as gc
import sys

def main():
    """
    Where all is ran in order
    """
    # assign the commandline arguments, and check if there are enough
    arguments = sys.argv
    if len(arguments) > 1:
        filename = arguments[1]
    else:
        raise Exception("too few arguments given")

    # extract the header and values from the csv file
    file_values_header = csv.xdata_extractor(filename)
    if arguments[2] == "barchart":
        gc.barchart(file_values_header)
    elif arguments[2] == "boxplot":
        gc.boxplot(file_values_header)

# to protect against problems if imported
if __name__ == "__main__":
    main()