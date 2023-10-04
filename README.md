# unidata

`unidata` is a Python library geared towards helping university research assistants with automating the cleaning of low quality data sets in preparation for advanced machine learning analysis.

Importing the `unidata` module allows you to use the `unidata` module's functions to automate the data cleaning process. 

## unidata benefits

As a university research assistant, you might be required to process, collate, and analyze data such as surveys surveys for the
research study coordinators. When you receive a survey from a research study participant, you are receiving
raw data. You might have to perform several tasks to make that raw data usable in the study coordinators'
research. 

An example task could be checking a file for invalid values or formatting columns so that you can
perform mathematical operations on those columns.

If you have a lot of data to process, munging that data programmatically is much more efficient than munging
that data manually. With a more automated solution, you can reduce your time spent processing each file and
the likelihood for human error

## Example: Using format_currency_entries()

Calling the `format_currency_entries()` prepares raw data columns that contain unwanted characters for further
data analysis.

You can use `format_currency_entries()` to do the following:
  + Remove the dollar sign ($) from specified column values.
  + Convert the values in any specified columns from the `object` data type to the `float64` data type.
  + Round each value in specified columns to the nearest hundredth.
