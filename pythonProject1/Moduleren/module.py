"""
Graph creator program
Author: Delshad Vegter
Date:6-12-22
"""

import csvreader as csv
import bargraphcreator as bgc
import sys

def main():

    # assign the commandline arguments, and check if there are enough
    arguments = sys.argv
    if len(arguments) > 1:
        filename = arguments[1]
    else:
        raise Exception("too few arguments given")

    # extract the header and values from the csv file
    file_values_header = csv.xdata_extractor(filename)
    if arguments[2] == "bar_chart":
        bgc.barchart(file_values_header)

if __name__ == "__main__":
    main()