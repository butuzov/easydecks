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

Verbs Card

```python
import easydecks as ed

deck = ed.Deck("Duo.Deu.Basics_Verbs")
deck.card(
  "verbs",
  "verstehen",
  "to understand",
  "Sie ... es nicht",
  'Sie <strong><span class="base">versteh</span><span class="changed">en</span></strong> es nicht',
  '<strong>verben</strong> - <strong>Sie verb<span class="changed">en</span></strong>',
  '<strong>verstehen</strong> - <strong>Sie versteh<span class="changed">en</span></strong>')

deck.save(__file__.replace(".py", ""))
```

```

* [ ] Docs
* [ ] Tests
* [ ] TODO: Media (Pictures and Sound)
