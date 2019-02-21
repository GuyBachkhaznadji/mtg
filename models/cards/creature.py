from .card import Card


class Creature(Card):

    def __init__(self, name, colour, cost, creature_types, power, toughness):
        Card.__init__(self, name, colour, cost)
        self.tapped = False
        self.creature_types = creature_types
        self.power = power
        self.toughness = toughness
        self.summoningSickness = True
        self.attacking = False
