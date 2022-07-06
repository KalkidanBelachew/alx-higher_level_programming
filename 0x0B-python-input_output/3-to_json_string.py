#!/usr/bin/python3
"""Module 3-write_file.
Writes in a text file.
"""
import json


def to_json_string(my_obj):
    """
    Returs a json string containing object's representation
    Arguments:
        my_obj (str): The inputed object to convert in json format
    Return:
        A json format text
    """
    return json.dumps(my_obj)
