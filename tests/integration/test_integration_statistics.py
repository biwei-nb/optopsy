from optopsy.option_strategies import long_call, short_call, long_put, short_put
from optopsy.data import get
from optopsy.statistics import results
from datetime import datetime
import os
import pytest

CURRENT_FILE = os.path.abspath(os.path.dirname(__file__))
TEST_FILE_PATH_FULL = os.path.join(
    CURRENT_FILE, "../test_data/test_options_data_full.csv"
)

hod_struct = (
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

DATA = get(TEST_FILE_PATH_FULL, hod_struct, prompt=False)


def test_win_count():
    filters = {
        "start_date": datetime(2018, 1, 1),
        "end_date": datetime(2018, 2, 28),
        "entry_dte": 31,
        "leg1_delta": 0.30,
        "exit_dte": 7,
    }

    backtest = long_call(DATA, filters)
    print(results(backtest, filters))
    assert results(backtest, filters) == {
        "Profit": 9330.0,
        "Win Percent": 0.5,
        "Loss Percent": 0.5,
        "Trades": 2,
        "start_date": datetime(2018, 1, 1),
        "end_date": datetime(2018, 2, 28),
        "entry_dte": 31,
        "leg1_delta": 0.30,
        "exit_dte": 7,
    }
