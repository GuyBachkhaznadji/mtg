from .card import Card


class Sorcery(Card):

    def __init__(self, name, colour, cost):
        Card.__init__(self, name, colour, cost)
