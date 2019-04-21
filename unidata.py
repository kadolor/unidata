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
"""@package unidata
Documentation for unidata.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import pandas as pd


def remove_character_from_column(data_frame, character, *columns):
    """Removes <code>character</code> from <code>*columns</code> in
    <code>data_frame</code>.
    
    Args:
        <code>data_frame</code>: A pandas DataFrame.
        <code>character</code>: The character you want to remove.
        <code>*columns<code>: The name(s) of the column(s) that contain the
        <code>character</code> that you want to remove. <code>*columns</code>must be
        formatted as <code>object</code>.
    """
    for each_column in columns:
        data_frame[each_column] = data_frame[each_column].str.replace(
            character, "")


def get_column_names(data_frame):
    """Returns a list of every column name in <code>data_frame</code>.

    Args:
        <code>data_frame</code>: A pandas DataFrame.
    Returns:
        A list of every column name in <code>data_frame</code>.
    """
    column_names = data_frame.columns.get_values()
    return column_names


def round_column(data_frame, *columns):
    """Rounds the <code>*columns</code> in <code>data_frame</code> to the 
    nearest hundredth. 

    Args:
        <code>data_frame</code>: A pandas DataFrame.
        <code>*columns</code>: The name(s) of the column(s) that you want
        to round. <code>*columns</code> must be formatted as float64.

    """
    for arg in columns:
        if data_frame[arg].dtype == "float64":
            data_frame[arg] = data_frame[arg].round(decimals=2)
        elif data_frame[arg].dtype != "float64":
            pass


def create_float_values(data_frame, *columns):
    """Converts values to the float64 data type. 

    Args:
        <code>data_frame</code>: A pandas DataFrame.
        <code>*columns</code>: The name(s) of the column(s) or convert 
        to float64. 
    """
    for arg in columns:
        data_frame[arg] = pd.to_numeric(data_frame[arg])
        data_frame[arg].astype(dtype=float)


def format_currency_entries(data_frame, character="$", *columns):
    """Formats <code>*columns</code> in the following ways: 
    - Removes currency symbol.
    - Converts <code>*columns</code> to float64.
    - Rounds <code>*columns</code> to the nearest hundredth.

    Args:
        <code>data_frame</code>: A pandas DataFrame.
        <code>character</code>: The currency symbol that you want to remove.
        Defaults to $.
        <code>*columns</code>: The name(s) of the column(s) that you want to format.
        Columns included in <code>*columns</code> must have the <code>object</code> data type.
    """
    for column in columns:
        remove_character_from_column(data_frame, character, column)
        create_float_values(data_frame, column)
        round_column(data_frame, column)


def check_column_for_negatives(data_frame, *columns):
    """Checks <code>*columns</code> in <code>data_frame</code>
    for negative values.

    Args:
        <code>data_frame</code>: A pandas DataFrame.
        <code>*columns</code>: The name(s) of the float64 column(s) that you
        want to check for negative values.
    Raises:
        ValueError: If columns are found to contain negative values.

    """
    for column in columns:
        if data_frame[column].dtype == "float64":
            for value in data_frame[column]:
                if value < 0:
                    raise ValueError(
                        "A column in this DataFrame contains negative values. "
                        + "Review the original data file.")
