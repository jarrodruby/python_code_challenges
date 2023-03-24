# n the first round,
# your opponent will choose Rock (A),
# and you should choose Paper (Y).
# This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X).
# This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
from dataclasses import dataclass

from functools import reduce

class BaseMove():
    def __init__(self, points):
        self.points = points

    def __int__(self):
        return self.points


class Rock(BaseMove):
    def play(self, other):
        return {
            Rock: "draw",
            Paper: "loss",
            Scissors: "win"
        }[other.__class__]


class Paper(BaseMove):
    def play(self, other):
        return {
            Rock: "win",
            Paper: "draw",
            Scissors: "loss"
        }[other.__class__]


class Scissors(BaseMove):
    def play(self, other):
        return {
            Rock: "loss",
            Paper: "win",
            Scissors: "draw"
        }[other.__class__]


def play_round(player_round):
    POINTS = {'win': 6, 'loss': 3, 'draw': 0, }
    CODE_TO_MOVE = {
        'A': Rock(1), 'B': Paper(2),
        'C': Scissors(3), 'X': Rock(1),
        'Y': Paper(2), 'Z': Scissors(3),
    }

    opponent_move, my_move = CODE_TO_MOVE.get(player_round[0]), CODE_TO_MOVE.get(player_round[1])
    return POINTS[my_move.play(opponent_move)] + int(my_move)

def run_strategy(strategy):
    round_scores = map(play_round, strategy)
    return sum(round_scores)

