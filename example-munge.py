import pandas as pd
import numpy as np

import unidata as ud


def main():
    """Reads in coffee-survey.csv and prints a DataFrame with columns formatted
    by format_currency_entries().
    """
    participant_data = pd.read_csv("coffee-survey.csv", dtype=str)
    ud.format_currency_entries(
        participant_data,
        ["Dollars Spent", "How much did you spend on coffee?"])
    print(participant_data)


if __name__ == '__main__':
    main()
