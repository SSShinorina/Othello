from AlphaBeta import AlphaBeta
from CountingEvaluator import CountingEvaluator
from OthelloAction import OthelloAction
from OthelloPosition import OthelloPosition


class Othello:
    def __init__(self, othello_position, alpha_beta, othello_action, value):
        value = "WEEEEEEEEEEEEEEEEEEEEEEEEEEEOXEEEEEEXOEEEEEEEEEEEEEEEEEEEEEEEEEEE"
        othello_action = OthelloAction.print_move
        othello_position = OthelloPosition.print_board
        alpha_beta = AlphaBeta.evaluate(CountingEvaluator)



