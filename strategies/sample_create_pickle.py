# This file is used to merge csv data across multiple files and create one
# pickle file to store all the data


import optopsy as op
import os
import pandas as pd

def store_data(file_name):
    
    SPX_FILE_STRUCT = (
        ("underlying_symbol", 0),
        ("underlying_price", 1),
        ("option_type", 5),
        ("expiration", 6),
        ("quote_date", 7),
        ("strike", 8),
        ("bid", 10),
        ("ask", 11),
        ("delta", 15),
        ("gamma", 16),
        ("theta", 17),
        ("vega", 18),
    )

    # absolute file path to our input file
    curr_file = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(curr_file, "data", f"{file_name}.pkl")

    # check if we have a pickle store
    if os.path.isfile(file):
        print("pickle file found, retrieving...")
        return pd.read_pickle(file)
    else:
        print("no picked file found, retrieving csv data...")

        csv_dir = os.path.join(curr_file, "data")
        data = op.get(csv_dir, SPX_FILE_STRUCT, prompt=False)

        print("storing to pickle file...")
        pd.to_pickle(data, file)
        return data


if __name__ == "__main__":
    # calling results function from the results returned from run_strategy()
    r = store_data("SPX_2014_2018")
    print(r.head())

