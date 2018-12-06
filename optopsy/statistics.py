#     Optopsy - Python Backtesting library for options trading strategies
#     Copyright (C) 2018  Michael Chu

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np
from pandas.core.base import PandasObject


def calc_ending_balance(data, init_balance):
    window = np.insert(data["cost"].values, 0, init_balance, axis=0)
    return np.subtract.accumulate(window)[-1]


def calc_total_trades(data):
    return data.index.max() + 1


def calc_total_profit(data):
    return data["cost"].sum().round(2) * -1


def extend_pandas():
    pass
