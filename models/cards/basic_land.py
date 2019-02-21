from .card import Card


class BasicLand(Card):

    def __init__(self, name, colour, cost):
        Card.__init__(self, name, colour, cost)
        self.tapped = False
