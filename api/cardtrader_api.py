from typing import Any

import requests


class CardtraderAPI:
    @staticmethod
    def __get_products_url(expansion_id: int) -> str:
        return f'https://api.cardtrader.com/api/v2/marketplace/products?expansion_id={expansion_id}'

    @staticmethod
    def __get_all_expansions_url() -> str:
        return f'https://api.cardtrader.com/api/v2/expansions'

    @staticmethod
    def __get_data(url, api_key):
        headers = {"Authorization": f"Bearer {api_key}"}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()

    @classmethod
    def get_all_expansions(cls, api_key: str) -> list[dict[str, Any]]:
        expansions_url = cls.__get_all_expansions_url()
        all_expansions = cls.__get_data(expansions_url, api_key)
        return all_expansions

    @classmethod
    def get_products_by_expansion(cls, api_key: str, expansion_id: int) -> dict[str, list[str, Any]]:
        products_url = cls.__get_products_url(expansion_id)
        products = cls.__get_data(products_url, api_key)
        return products
