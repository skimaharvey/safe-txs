import logging

import requests

from .exceptions import CannotGetPrice

logger = logging.getLogger(__name__)


class BinanceClient:  # pragma: no cover
    def __init__(self):
        self.http_session = requests.Session()

    def _get_price(self, symbol: str):
        url = "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=LYXE-USDT"

        try:
            response = self.http_session.get(url, timeout=10)
            result = response.json()
            return float(result["data"]["price"])
        except (ValueError, IOError) as e:
            logger.warning("Cannot get price from url=%s", url)
            raise CannotGetPrice from e

    def get_ada_usd_price(self) -> float:
        return self._get_price("ADAUSDT")

    def get_aurora_usd_price(self):
        return self._get_price("NEARUSDT")

    def get_bnb_usd_price(self) -> float:
        return self._get_price("BNBUSDT")

    def get_ether_usd_price(self) -> float:
        """
        :return: current USD price for Ethereum
        :raises: CannotGetPrice
        """
        return self._get_price("ETHUSDT")

    def get_matic_usd_price(self) -> float:
        """
        :return: current USD price for MATIC
        :raises: CannotGetPrice
        """
        return self._get_price("MATICUSDT")
