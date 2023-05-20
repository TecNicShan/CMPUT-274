"""
--------------------------------------------
Name: Nick Shan
SID: 1759726
CCID: bshan1
AnonID: 1000366406
CMPUT 274, Fall 2022

Assessment: Weekly Exercise #3
--------------------------------------------

FREQ TEMPLATE: ADD YOUR INFORMATION TO ABOVE

You must determine how to structure your solution.
Create your functions here and call them from under
if __name__ == "__main__"!
"""

import sys


def check_inputs():
    # print(sys.argv[0])
    if len(sys.argv) < 2:
        return None
    if len(sys.argv) > 2:
        return False
    else:
        return True


def file_open(filename):
    file = open(filename, "r")
    contents = file.read()
    contents = "".join(contents)
    contents = contents.split(" ")
    contents = [string.split("\n") for string in contents]
    contents = [item for x in contents for item in x]
    file.close()
    return contents


def counter(word_list):
    total_words = 0
    freq = {}
    for x in word_list:
        if x == "":
            continue
        if x not in freq:
            freq[x] = 0
        freq[x] += 1
        total_words += 1
    freq = sorted(freq.items())
    return freq, total_words


def out(frequency_list, filename, num_total_words):
    out_file = open(filename + ".out", "w")
    for x in frequency_list:
        out_file.write(x[0] + " " + str(x[1]) + " " +
                       str(round((x[1] / num_total_words), 3)))
        out_file.write("\n")

    out_file.close()
    # print(contents)
    # print(filename)
    return (out_file)


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.
    if check_inputs() is True:
        filename = sys.argv[1]
        contents = file_open(filename)
        freq_list = counter(contents)[0]
        num_words = counter(contents)[1]
        out(freq_list, filename, num_words)
    if check_inputs() is False:
        print("Too many arguments. Usage: python3 freq.py <input file name>")
        exit()
    if check_inputs() is None:
        print("Too few arguments. Usage: python3 freq.py <input file name>")
        exit()
