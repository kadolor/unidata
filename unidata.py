# MIT License

# Copyright (c) 2019 Kelly-Ann R. Dolor

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import pandas as pd


def remove_character_from_column(data_frame, character, *columns):
    """Removes character from specified float64 columns in data_frame.
    
    Args:
        data_frame: A pandas.DataFrame.
        character: The character that you want to remove.
        *columns: The names of the columns that contain the
        character that you want to remove.
        *columns parameters must be passed as strings
        and the column arguments must have the object data type.
    Raises:
        ValueError: If *columns parameters are not passed as strings.
        ValueError: If *columns arguments do not have the object data type.
    """
    for each_column in columns:
        if type(each_column) != str:
            raise ValueError(each_column + " must be passed a string.")
        if data_frame[each_column].dtype == "object":
            data_frame[each_column] = data_frame[each_column].str.replace(
                character, "")
        else:
            raise ValueError(each_column + " column argument must have the object data type.")


def get_column_names(data_frame):
    """Returns a list of every column name in data_frame.

    Args:
        data_frame: A pandas.DataFrame.
    Returns:
        A list of every column name in data_frame.
    """
    data_frame.columns.get_values()
    
    return data_frame.columns.get_values()


def round_column(data_frame, *columns):
    """Rounds the specifed float64 columns in data_frame
    to the nearest hundredth. 

    Args:
        data_frame: A pandas.DataFrame.
        *columns: The names of the columns that contain the values 
        that you want to round. *columns parameters must be passed 
        as strings and the column arguments must have the float64 
        data type.
    Raises:
        ValueError: If *columns parameters are not passed as strings.
        ValueError: If *columns arguments do not have the float64 data type.

    """
    for each_column in columns:
        if type(each_column) != str:
            raise ValueError(each_column + " must be passed a string.")
        if data_frame[each_column].dtype == "float64":
            data_frame[each_column] = data_frame[each_column].round(decimals=2)
        else:
            raise ValueError(each_column + " column argument must have the float64 data type.")


def create_float_values(data_frame, *columns):
    """Converts values in specified columns in data_frame to the
    float64 data type. 

    Args:
        data_frame: A pandas.DataFrame.
        *columns: The names of the columns that contain the values 
        that you want to convert to the float64 data type. *columns parameters 
        must be passed as strings.
    Raises:
        ValueError: If *columns parameters are not passed as strings.
    """
    for each_column in columns:
        if type(each_column) != str:
            raise ValueError(each_column + " must be passed a string.")
    for each_column in columns:
        data_frame[each_column] = pd.to_numeric(data_frame[each_column])
        data_frame[each_column].astype(dtype=float)


def format_currency_entries(data_frame, character="$", *columns):
    """Formats data_frame columns in the following ways: 
    - Removes currency symbol.
    - Converts data_frame columns to float64.
    - Rounds data_frame columns to the nearest hundredth.

    Args:
        data_frame: A pandas.DataFrame.
        character: The currency symbol that you want to remove.
        character defaults to "$".
        *columns: The names of the columns that you want to format.
        *columns parameters must be passed as strings and the
        column arguments must have the object data type.
    Raises:
        ValueError: If *columns parameters are not passed as strings.
    """
    for each_column in columns:
        if type(each_column) != str:
            raise ValueError(each_column + " must be passed a string.")

    for column in columns:
        remove_character_from_column(data_frame, character, column)
        create_float_values(data_frame, column)
        round_column(data_frame, column)


def verify_positive_values(data_frame, *columns):
    """Verifies that specifed columns in data_frame have only positive values.

    Args:
        data_frame: A pandas.DataFrame.
        *columns: The names of the float64 columns that you
        want to check for negative values. *columns parameters 
        must be passed as strings and the column arguments must have the 
        float64 or int64 data type.
    Raises:
        ValueError: If *columns parameters are not passed as strings.
        ValueError: If values in column arguments contain negative values.
    """
    for each_column in columns:
        if type(each_column) != str:
            raise ValueError(each_column + " must be passed a string.")

    for each_column in columns:
        if data_frame[each_column].dtype == "float64" or "int64":
            for value in data_frame[each_column]:
                if value < 0:
                    raise ValueError(each_column +
                        " column contains negative values.")