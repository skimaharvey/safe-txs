import logging

import requests

from .exceptions import CannotGetPrice

logger = logging.getLogger(__name__)


class KrakenClient:
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
        return self._get_price("ADAUSD")

    def get_avax_usd_price(self) -> float:
        """
        :return: current USD price for AVAX
        :raises: CannotGetPrice
        """
        return self._get_price("AVAXUSD")

    def get_dai_usd_price(self) -> float:
        """
        :return: current USD price for DAI
        :raises: CannotGetPrice
        """
        return self._get_price("DAIUSD")

    def get_ether_usd_price(self) -> float:
        """
        :return: current USD price for Ethereum
        :raises: CannotGetPrice
        """
        return self._get_price("ETHUSD")

    def get_matic_usd_price(self):
        """
        :return: current USD price for MATIC
        :raises: CannotGetPrice
        """
        return self._get_price("MATICUSD")

    def get_ewt_usd_price(self) -> float:
        """
        :return: current USD price for Energy Web Token
        :raises: CannotGetPrice
        """
        return self._get_price("EWTUSD")

    def get_algo_usd_price(self):
        """
        :return: current USD price for Algorand
        :raises: CannotGetPrice
        """
        return self._get_price("ALGOUSD")
