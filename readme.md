# `easydecks` - genanki's wrapper with benefits.

![](https://butuzov.github.io/easydecks/preview.png)

## Why?

It's allows to create [anki](https://apps.ankiweb.net/) desk faster, and easier. We proudly standing on the shoulders of [giants](https://github.com/kerrickstaley/genanki).

## Examples.

Using [`slovo`](https://github.com/butuzov/slovo)

```python3
import slovo
import easydecks as ed

Deu = slovo.Word.constr("Deu", "de")
Eng = slovo.Word.constr("Eng", "en")

deck = ed.Deck("Duo.Deu.Basics_I&II")
deck.card('DEFAULT').default(
    Eng("Are you sick?").image("images/you_are_ill.jpg"),
    Deu("Bist du krank?").image("images/you_are_ill.jpg"),
)

deck.save(__file__.replace(".py", ""))
```

Simple cards

```python
import easydecks as ed

deck = ed.Deck("Duo.Deu.Basics_I&II")
deck.card('DEFAULT').default(
    "Are you sick?",
    "Bist du krank?",
)

deck.save(__file__.replace(".py", ""))
```

* [ ] TODO: Custom Card Class
* [ ] TODO: Media (Pictures and Sound)
