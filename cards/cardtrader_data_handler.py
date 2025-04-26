from typing import Any

from cards.card_data import Card


class CardtraderDataHandler:

    @staticmethod
    def parse_cards(cards: list[dict[str, Any]]) -> list[Card]:
        expansion_cards = []
        for card in cards:
            expansion_cards.append(Card(expansion=card['expansion'].get(f'name_en', ''),
                                        expansion_shortcut=card['expansion'].get(f'code', ''),
                                        name=card.get(f'name_en', ''),
                                        language=next((card['properties_hash'][key] for key in card['properties_hash'] if key.endswith('_language')), None),
                                        rarity=next((card['properties_hash'][key] for key in card['properties_hash'] if key.endswith('_rarity')), None),
                                        collector_number=card['properties_hash'].get('collector_number', ''),
                                        price_cents=card['price'].get('cents'),
                                        foil=next((card['properties_hash'][key] for key in card['properties_hash'] if key.endswith('_foil')), None),
                                        condition=card['properties_hash'].get('condition', '')))
        return expansion_cards

    @staticmethod
    def get_expansion_id(all_expansions: list[dict[str, Any]], expansion_name) -> int:
        for expansion in all_expansions:
            if expansion.get('name') == expansion_name:
                return expansion.get('id')
        raise ValueError(f'No expansion could be found for given expansion name {expansion_name}')

    @staticmethod
    def flatten_products(products: dict[str, list[str, Any]]) -> list[dict[str, Any]]:
        flattened_products = []
        for sublist in list(products.values()):
            for item in sublist:
                flattened_products.append(item)
        return flattened_products

    @staticmethod
    def filter_by_language(cards: list[Card], language: str) -> list[Card]:
        filtered_cards = []
        for card in cards:
            if card.language == language:
                filtered_cards.append(card)
        return filtered_cards

    @staticmethod
    def filter_by_condition(cards: list[Card], condition: str) -> list[Card]:
        filtered_cards = []
        for card in cards:
            if card.condition == condition:
                filtered_cards.append(card)
        return filtered_cards

    @staticmethod
    def filter_by_collection_number(cards: list[Card], collection_number: str) -> list[Card]:
        filtered_cards = []
        for card in cards:
            if card.collector_number == collection_number or card.collector_number == str(int(collection_number)):
                filtered_cards.append(card)
        return filtered_cards

    @staticmethod
    def filter_by_foil(cards: list[Card], foil: bool) -> list[Card]:
        filtered_cards = []
        for card in cards:
            if card.foil == foil:
                filtered_cards.append(card)
        return filtered_cards

    @staticmethod
    def get_average_cheapest_cards(cards: list[Card], count: int) -> float:
        sorted_cards = sorted(cards, key=lambda card: card.price_cents)
        cheapest_cards = sorted_cards[:count]
        average_price = sum([card.price_cents for card in cheapest_cards])/len(cheapest_cards)
        return average_price



