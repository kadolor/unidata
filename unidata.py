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


# Remember two lines between functions
def remove_character_from_column(data_frame, character, *columns):
    """Removes @character from @columns in @data_frame.
    
    Args:
        data_frame: A pandas DataFrame.
        character: The character you want to remove.
        *column: The string column or columns you want to remove the character from.
    """
    for each_column in columns:
        data_frame[each_column] = data_frame[each_column].str.replace(
            character, "")


def get_column_names(data_frame):
    """Returns a list of every column name in @data_frame.

    Args:
        data_frame: A pandas DataFrame.
    Returns:
        Returns a list of every column name in @data_frame.
    """
    column_names = data_frame.columns.get_values()
    return column_names


def round_column(data_frame, *columns):
    """Rounds float64 @*columns in @data_frame to the nearest hundredth. 

    Args:
        data_frame: A pandas DataFrame.
        *columns: The float64 column or columns you want to round. 

    Returns: 
    """
    for arg in columns:
        if data_frame[arg].dtype == "float64":
            data_frame[arg] = data_frame[arg].round(decimals=2)
        elif data_frame[arg].dtype != "float64":
            pass


def create_float_values(data_frame, *columns):
    """Sets @data_frame @*columns to float64 numerical type. 

    Args:
        data_frame: A pandas DataFrame.
        *columns: The column or columns set to float64 numerical type. 
    """
    for arg in columns:
        data_frame[arg] = pd.to_numeric(data_frame[arg])
        data_frame[arg].astype(dtype=float)


def format_currency_entries(data_frame, character="$", *columns):
    """Formats @columns in the following ways: 
    - Removes currency symbol.
    - Sets @columns to float64.
    - Rounds @columns to the nearest hundredth.

    Args:
        data_frame: A pandas DataFrame.
        character: The currency symbol you want to remove. Defaults to $.
        *columns: The string column or columns you want formatted. 
    Raises
    """
    for column in columns:
        remove_character_from_column(data_frame, character, column)
        create_float_values(data_frame, column)
        round_column(data_frame, column)


def check_column_for_negatives(data_frame, *columns):
    """Checks @columns in @data_frame for negative values.

    Args:
        data_frame: A pandas DataFrame.
        *columns: Float64 columns to check for negative values.
    Raises:
        ValueError

    """
    for column in columns:
        if data_frame[column].dtype == "float64":
            for value in data_frame[column]:
                if value < 0:
                    raise ValueError(
                        "A column in this DataFrame contains negative values. "+
                        "Review the original data file."
                    )
