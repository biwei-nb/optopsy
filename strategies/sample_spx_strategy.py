import os
from datetime import datetime
import pandas as pd
import optopsy as op


def run_strategy():

    # grab our data created from sample_create_pickle.py
    curr_file = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(curr_file, "data", "SPX_2014_2018.pkl")
    data = pd.read_pickle(file)

    # define the entry and exit filters to use for this strategy, full list of
    # filters will be listed in the documentation (WIP).
    filters = {
        # set the start and end dates for the backtest,
        # the dates are inclusive, and are python datetime objects.
        "start_date": datetime(2018, 1, 1),
        "end_date": datetime(2018, 12, 31),
        "entry_dte": (40, 47, 50),
        "leg1_delta": 0.30,
        "leg2_delta": 0.50,
        "leg3_delta": 0.50,
        "leg4_delta": 0.30,
        "contract_size": 1,
        "expr_type": "SPX",
    }

    # strategy functions will return a dataframe containing all the simulated trades
    spreads = op.long_iron_condor(data, filters)
    
    # get the profits of this strategy
    print(f"Total Profit: {spreads.total_profit()}")

if __name__ == "__main__":
    run_strategy()
