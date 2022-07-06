#!/usr/bin/python3
"""Module 2-append_file.
Writes in a text file.
"""



def append_write(filename="", text=""):
    """
    Appends inputed text into a utf-8 encoded text file
    Arguments:
        filename (str): The name of the file to open
        text (str): The text to append
    Return:
        A file with appened text
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
