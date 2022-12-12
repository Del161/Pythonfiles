"""
creates bar graphs from values
Author: Delshad Vegter
date: 6-12-22
"""

import matplotlib.pyplot as plt


def barchart(values_headers):
    """
    this is what will make the barchart
    :param values_headers: a tuple with 2 lists
    :return:
    """
    user_choice = category_chooser(values_headers)
    barchart_creator(values_headers, user_choice)


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
        user_choice = input("please enter the value of the wanted category: ")

    return user_choice


def barchart_creator(values_headers, user_choice):
    """
    Creates a bar chart from the given values.
    :param values_headers: a tuple with 2 lists
    :param user_choice: integer with user choice
    :return: a barchart
    """
    labels = values_headers[0]
    tick_labels = []
    tick_values = []
    headers = values_headers[1]

    for individual_labels in labels:
        individual_values = labels[individual_labels]
        tick_values.append(int(individual_values[int(user_choice)]))
        tick_labels.append(individual_labels)

    x_axis = tick_labels
    height = tick_values

    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.85, 0.85])
    fig.autofmt_xdate()
    ax.bar(x_axis, height)
    plt.show()


def main():
    """
    one who rules
    """
    print("you aren't supposed to run this")


# to protect against problems when imported
if __name__ == "__main__":
    main()
