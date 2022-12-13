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
    values = values_headers[0]
    tick_labels = []
    tick_values = []

    for individual_labels in values:
        individual_values = values[individual_labels]
        tick_values.append(int(individual_values[int(user_choice)]))
        tick_labels.append(individual_labels)

    x_axis = tick_labels
    height = tick_values

    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.85, 0.85])
    fig.autofmt_xdate()
    ax.bar(x_axis, height)
    plt.show()


def boxplot(values_headers):
    """
    Creates a boxplot from the given values
    """

    # predefined variables
    headers_numerated = []
    values = values_headers[0]
    headers1 = values_headers[1]
    tick_values = []
    data = []
    plot_data = []
    counter = 0
    user_choice = ""
    x_labels = []

    for headers in headers1[1:]:
        headers_numerated.append(str(counter) + " : " + headers + "\n")
        counter += 1

    if len(headers1) > 2:
        print("There are multiple values, please select the ones you want to use for the bar chart\n"
              "the input method is 1,2,3,4 etc or 1,4,6 etc, use * for all categories \n",
              *headers_numerated)
        user_choice = input("please enter the values of the wanted categories: ")

    # make the lists for use in the boxplot
    for count in range(len(headers1[1:])):
        for individual_labels in values:
            individual_values = values[individual_labels]
            tick_values.append(int(individual_values[int(count)]))
        data.append(tick_values)
        tick_values = []

    # act upon user choice
    if user_choice == "*":
        plot_data = data
        x_labels = headers1[1:]
    else:
        user_choice = user_choice.split(",")
        for numbers in user_choice:
            plot_data.append(data[int(numbers)])
            x_labels.append(headers1[int(numbers)+1])

    # plot the boxplot with all the data
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_axes([0.15, 0.15, 0.85, 0.85])
    ax.set_xticklabels(x_labels)
    plt.setp(ax.get_xticklabels(), rotation=10, horizontalalignment='right')

    bp = ax.boxplot(plot_data)
    plt.show()

def main():
    """
    one who rules
    """
    print("graphcreator.py main")


# to protect against problems when imported
if __name__ == "__main__":
    main()
