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
import json

from octobot_channels.channels.channel import get_chan

from octobot_commons.channels_name import OctoBotBacktestingChannelsName
from octobot_trading.producers.ticker_updater import TickerUpdater


class TickerUpdaterSimulator(TickerUpdater):
    def __init__(self, channel):
        super().__init__(channel)
        self.exchange_data_importer = self.channel.exchange_manager.exchange.backtesting.importers[0]  # TODO TEMP
        self.exchange_name = self.channel.exchange_manager.exchange.name
        self.last_timestamp_pushed = 0

    async def start(self):
        await get_chan(OctoBotBacktestingChannelsName.TIME_CHANNEL.value).new_consumer(self.handle_timestamp)

    async def handle_timestamp(self, timestamp: int):
        try:
            # TODO foreach symbol
            ticker_data = self.exchange_data_importer.get_ticker_from_timestamps(exchange_name=self.exchange_name,
                                                                                     symbol="BTC/USDT",
                                                                                     inferior_timestamp=timestamp,
                                                                                     limit=1)[0]
            if ticker_data[0] > self.last_timestamp_pushed:
                self.last_timestamp_pushed = ticker_data[0]
                await self.push(ticker_data[-3], json.loads(ticker_data[-1]))
        except IndexError as e:
            self.logger.warning(f"Failed to access ticker_data : {e}")
