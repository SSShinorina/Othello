from CountingEvaluator import CountingEvaluator
from OthelloPosition import OthelloPosition


class Othello:
    def othello(black_strategy, white_strategy):
        #
        board = OthelloPosition.initialize()
        player = 'B'
        strategy = lambda who: black_strategy if who == 'B' else white_strategy
        while player is not None:
            move = OthelloPosition.get_moves(board)
            OthelloPosition.make_move(move, player, board)
            player = OthelloPosition.to_move(board)
        return board, CountingEvaluator.evaluate(board)



