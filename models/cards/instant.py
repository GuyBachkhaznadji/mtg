from .card import Card


class Instant(Card):

    def __init__(self, name, colour, cost):
        Card.__init__(self, name, colour, cost)
