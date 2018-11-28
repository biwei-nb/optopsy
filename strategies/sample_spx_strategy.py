import os
from datetime import datetime
import pandas as pd
import optopsy as op


def run_strategy():
    
    # grab our data
    curr_file = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(curr_file, "data", "SPX_2014_2018.pkl")
    data = pd.read_pickle(file)
    
    # define the entry and exit filters to use for this strategy, full list of
    # filters will be listed in the documentation (WIP).
    filters = {
        "entry_dte": (6, 7, 8),
        "leg1_delta": 0.50,
        "leg2_delta": 0.30,
        "leg3_delta": 0.30,
        "leg4_delta": 0.50,
        "contract_size": 1,
        "expr_type": "SPX",
    }

    # set the start and end dates for the backtest, the dates are inclusive,
    # start and end dates are python datetime objects.
    # strategy functions will return a dataframe containing all the simulated trades
    spreads = op.long_iron_condor(data, filters)

    # calling results function from the results returned from run_strategy()
    results = op.results(spreads, filters)
    print(results)


if __name__ == "__main__":
    run_strategy()
