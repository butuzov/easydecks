from __future__ import annotations

from typing import List
from os.path import basename, dirname
from re import compile

import genanki


def __init__(*args, **kwargs) -> Card:
    """
    module router
    """
    return Card(*args, **kwargs)


def read(filename):
    with open(filename, "r") as fh:
        return fh.read()
    return ""


class Card:

    def __init__(self, *args):
        self._args = args

        self._media = []

    def _model(self) -> genanki.Model:
        """ Wrapper for simple default model """

        fields = [{
            "name": "Verb"
        }, {
            "name": "Translation"
        }, {
            "name": "Question"
        }, {
            "name": "Answer"
        }, {
            "name": "Rule_Pattern"
        }, {
            "name": "Rule_Real"
        }]
        templates = [{
            "name": "Card",
            "qfmt": read(dirname(__file__) + "/front.html"),
            "afmt": read(dirname(__file__) + "/back.html"),
        }]
        style = read(dirname(__file__) + "/style.min.css")

        return genanki.Model(
            20200324,
            "Verbs",
            fields=fields,
            templates=templates,
            css=style,
        )

    def media(self) -> List[str]:
        """ not supported """
        return self._media

    def export(self) -> genanki.Note:
        return genanki.Note(
            model=self._model(),
            fields=[*self._args],
        )
