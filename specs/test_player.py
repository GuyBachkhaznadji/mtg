from mtg.models.player import Player


def test_get_starting_hand():
    player_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    newPlayer = Player('Guy', player_deck)
    expected_hand_size = 7
    expected_deck_size = 3
    result_hand_size = len(newPlayer.hand)
    result_deck_size = len(newPlayer.deck)
    assert expected_hand_size == result_hand_size
    assert expected_deck_size == result_deck_size
