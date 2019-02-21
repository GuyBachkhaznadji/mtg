from random import shuffle, sample


class Player:

    def __init__(self, name, deck):
        self.name = name
        self.life_points = 20
        self.deck = sample(deck, len(deck))
        self.hand = self.draw_cards(7)
        self.has_played_land = False
        self.graveyard = []
        self.land = []
        self.creatures = []
        self.enchantments = []
        self.artifacts = []

    def shuffle_deck(self):
        shuffle(self.deck)

    def draw_cards(self, number_of_cards):
        drawn_cards, deck_cards, = self.deck[0:
                                             number_of_cards:], self.deck[number_of_cards:]
        self.deck = deck_cards
        return drawn_cards

    def play_land(self, land_card):
        self.land.apend(land_card)

    def get_untapped_land(self):
        untapped_land = []
        for land in self.land:
            if not land.tapped:
                untapped_land.append(land)
        return untapped_land

    def set_has_played_land(has_played_land):
        self.has_played_land = has_played_land

    def add_lifepoints(num_to_add):
        self.life_points += num_to_add

    def remove_lifepoints(num_to_remove):
        self.life_points -= num_to_remove
