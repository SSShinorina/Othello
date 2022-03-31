from CountingEvaluator import CountingEvaluator
from OthelloAction import OthelloAction
from OthelloPosition import OthelloPosition
from AlphaBeta import AlphaBeta
import sys

if __name__ == "__main__":
    othello_position = sys.argv[1]
    time_limit = sys.argv[2]

    board = OthelloPosition(othello_position)
    # board.initialize()
    counting_evaluate = CountingEvaluator()
    alpha_beta = AlphaBeta.set_evaluator(board, counting_evaluate)
    othello_action = AlphaBeta.evaluate(board, othello_position)
    print(f"these are the arguments {sys.argv}")
    print(f"othello action {othello_action}")
    print(board)
