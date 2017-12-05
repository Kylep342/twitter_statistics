"""
This module hosts a useful function for converting lists into
dictionaries containing a frequency of each element in the input list.
"""


def ListToFreqDict(list):
    """
    This function takes a list as input and returns a dictionary with
    the frequency of each element in the list as a value.
    """
    freq_dict = {}
    for item in list:
        if freq_dict.__contains__(item):
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict
