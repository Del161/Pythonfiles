"""
creates bar graphs from values
Author: Delshad Vegter
date: 6-12-22
"""

import matplotlib.pyplot as plt
import numpy as np


def barchart(values_headers, user_labels):
    """
    this is what will make the barchart
    :param values_headers: a tuple with 2 lists
    :return:
    """
    user_choice = category_chooser(values_headers)
    marked_labels = set_labels(user_labels)
    barchart_creator(values_headers, user_choice, marked_labels)


def category_chooser(values_headers):
    """
    creates a barchart from given values
    :param values_headers:
    :return:
    """

    user_choice = 0
    counter = 0
    headers_numerated = []
    header = values_headers[1]

    for headers in header[1:]:
        headers_numerated.append(str(counter) + " : " + headers + "\n")
        counter += 1

    if len(header) > 2:
        print("There are multiple values, please select the one you want to use for the bar chart\n",
              *headers_numerated)
        user_choice = input("please enter the value of the wanted category add an ,H to make the graph horizontal: ")

    return user_choice


def barchart_creator(values_headers, user_choice, marked_labels):
    """
    Creates a bar chart from the given values.
    :param values_headers: a tuple with 2 lists
    :param user_choice: integer with user choice
    :return: a barchart
    """
    values = values_headers[0]
    tick_labels = []
    tick_values = []
    hv_choice = ""

    user_choice = user_choice.split(",")
    if len(user_choice) > 1:
        hv_choice = user_choice.pop(-1)

    for individual_labels in values:
        individual_values = values[individual_labels]
        tick_values.append(int(individual_values[int(user_choice[0])]))
        tick_labels.append(individual_labels)

    x_axis = tick_labels
    height = tick_values

    fig, ax = plt.subplots()
    plt.title(marked_labels[2])
    ax.set_ylabel(marked_labels[0])
    ax.set_xlabel(marked_labels[1])

    if hv_choice == "H":
        # stuff to make the barchart horizontal if the user wishes so

        y_pos = np.arange(len(x_axis))
        ax.barh(x_axis, height, align='center')
        ax.set_yticks(y_pos, labels=x_axis)
        ax.invert_yaxis()  # labels read top-to-bottom
    else:
        # else just make it vertical
        fig.autofmt_xdate()
        ax.bar(x_axis, height)

    plt.show()


def boxplot(values_headers, user_labels):
    """
    runs the steps for the boxplot
    """
    plot_data, x_labels, hv_choice = make_lists(values_headers)
    marked_labels = set_labels(user_labels)
    plot_data_bx(plot_data, x_labels, hv_choice, marked_labels)


def make_lists(values_headers):
    """
    Makes lists to be used in he plot
    param: values_headers tuple with 2 lists
    """
    # predefined variables
    headers_numerated = []
    values = values_headers[0]
    headers1 = values_headers[1]
    tick_values = []
    data = []
    counter = 0
    user_choice = []
    plot_data = []
    hv_choice = True
    x_labels = []

    for headers in headers1[1:]:
        headers_numerated.append(str(counter) + " : " + headers + "\n")
        counter += 1

    # ask for user input what parts they want used
    if len(headers1) > 2:
        print("There are multiple values, please select the ones you want to use for the bar chart\n"
              "the input method is 1,2,3,4 etc or 1,4,6 etc, use * for all categories \n"
              "Add a capital H to make the plot horizontal example: 0,1,H \n",
              *headers_numerated)
        user_choice = input("please enter the values of the wanted categories: ")

    # make the lists for use in the boxplot
    for count in range(len(headers1[1:])):
        for individual_labels in values:
            individual_values = values[individual_labels]
            tick_values.append(int(individual_values[int(count)]))
        data.append(tick_values)
        tick_values = []

    # check if the user wants a vertical or horizontal plot
    user_choice = user_choice.split(",")
    if user_choice[-1] == "H":
        user_choice.pop(-1)
        hv_choice = False

    # check what parts of the data the user wants included
    if user_choice[0] == "*":
        plot_data = data
        x_labels = headers1[1:]
    else:
        for numbers in user_choice:
            plot_data.append(data[int(numbers)])
            x_labels.append(headers1[int(numbers) + 1])

    return plot_data, x_labels, hv_choice


def plot_data_bx(plot_data, x_labels, hv_choice, marked_labels):
    """
    Creates a boxplot from the given values
    param: plot_data a list with the data
    param: x_labels list with x axis labels
    param: hv_choice bool
    """

    # define fig and ax
    fig, ax = plt.subplots()

    # if the user wants verticals, make labels xaxis, else yaxis
    if hv_choice:
        ax.set_xticklabels(x_labels)
    else:
        ax.set_yticklabels(x_labels)

    ax.set_title(marked_labels[2])
    ax.set_ylabel(marked_labels[0])
    ax.set_xlabel(marked_labels[1])

    # set label alignment to prevent overlapping
    plt.setp(ax.get_xticklabels(), rotation=10, horizontalalignment='right')
    bp = ax.boxplot(plot_data, vert=hv_choice)
    plt.show()


def set_labels(user_labels):
    """
    creates the labels in plots
    param: user_labels string
    """

    labels = []

    # check and set labels
    labels = user_labels.split(",")
    ylabel = labels[0]
    xlabel = labels[1]
    title = labels[2]

    # make them empty if the user wants nothing there
    if ylabel == "*":
        ylabel = ""
    if xlabel == "*":
        xlabel = ""
    if title == "*":
        title = ""

    marked_labels = [ylabel, xlabel, title]
    return marked_labels


def main():
    """
    its main, what'd ya expect
    """
    print("graphcreator.py main")


# to protect against problems when imported
if __name__ == "__main__":
    main()
