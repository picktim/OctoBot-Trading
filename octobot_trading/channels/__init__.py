#  Drakkar-Software OctoBot-Trading
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.

from .balance import *
from .exchange_channel import *
from .kline import *
from .mode import *
from .ohlcv import *
from .order_book import *
from .orders import *
from .positions import *
from .recent_trade import *
from .ticker import *
from .trades import *

# Exchange public data
TICKER_CHANNEL = "Ticker"
RECENT_TRADES_CHANNEL = "RecentTrade"
ORDER_BOOK_CHANNEL = "OrderBook"
KLINE_CHANNEL = "Kline"
OHLCV_CHANNEL = "OHLCV"

# Exchange personal data
TRADES_CHANNEL = "Trades"
ORDERS_CHANNEL = "Orders"
BALANCE_CHANNEL = "Balance"
BALANCE_PROFITABILITY_CHANNEL = "BalanceProfitability"
POSITIONS_CHANNEL = "Positions"

# Internal
MODE_CHANNEL = "Mode"
