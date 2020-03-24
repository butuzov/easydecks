from __future__ import annotations

from typing import Callable

import genanki

from .cards import Cards


class Deck:

    default_card_type: str = "DEFAULT"

    def __init__(self, title):
        self._title: str = title
        self._cards = []
        self._types = Cards

    def register(self, key, card: Callable):
        self._types[key] = card

    def types(self) -> Cards:
        return self._types

    def default(self, *args, **kwargs) -> Callable:
        return self.card(self.default_card_type, *args, **kwargs)

    def card(self, card, *args, **kwargs) -> Callable:

        # if card.upper() == self.default_card_type:
        #     args = args[1:]

        self._cards.append(self._types[card].__init__(*args, **kwargs))
        return self._cards[-1]

    def _package(self) -> genanki.Package:
        deck = genanki.Deck(id(self._title), self._title)
        media = []
        for card in self._cards:
            media += card.media()
            deck.add_note(card.export())

        return genanki.Package(deck, media_files=media)

    def save(self, name):
        if ".apkg" not in name:
            name += ".apkg"
        self._package().write_to_file(name)
