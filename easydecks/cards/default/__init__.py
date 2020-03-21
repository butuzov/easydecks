from __future__ import annotations

from typing import List
from os.path import basename, dirname
from re import compile

import genanki


def __init__(*args, **kwargs) -> Card:
    """
    module router
    TODO: Write docs
    """
    return Card(*args, **kwargs)


def read(filename):
    with open(filename, "r") as fh:
        return fh.read()
    return ""


class Card:

    def __init__(self, question, answer, **kwargs):

        self._model = self._get_default_model() if 'model' not in kwargs else kwargs['model']
        self._media = []
        self._q = Field(question)
        self._a = Field(answer)

    def _get_default_model(self) -> genanki.Model:
        """ Wrapper for simple default model """

        fields = [{"name": "Question"}, {"name": "Answer"}]
        templates = [{
            "name": "Card",
            "qfmt": "<div class=question>{{Question}}</div>",
            "afmt": "<div class=answer>{{Answer}}</div>",
        }]
        style = read(dirname(__file__) + "/style.min.css")

        return genanki.Model(
            20200320,
            "Default Card Model",
            fields=fields,
            templates=templates,
            css=style,
        )

    def media(self) -> List[str]:

        return self._a.media + self._q.media

    def export(self) -> genanki.Note:
        return genanki.Note(
            model=self._model,
            fields=[str(self._q), str(self._a)],
        )


class Field:

    def __init__(self, value):

        self._image = value.get_image() if hasattr(value, 'get_image') else None
        self._sound = value.get_sound() if hasattr(value, 'get_sound') else None
        self._text = value.__html__() if hasattr(value, '__html__') else str(value)

    @property
    def media(self) -> List[str]:
        media = []
        if self._sound: media.append(self._sound)
        if self._image: media.append(self._image)

        return media

    def text(self, value: str):
        self._text = value

    def sound(self, sound: str):
        self._sound = sound

    def image(self, image: str):
        self._image = image

    def __str__(self) -> str:
        return "<figure>%s%s%s</figure>" % (
            ("<img src='%s'/>" % basename(self._image)) if self._image else "",
            ("[sound:%s]" % basename(self._sound)) if self._sound else "",
            ("<figcaption>%s</figcaption>" % self._text) if self._text != "" else "",
        )
