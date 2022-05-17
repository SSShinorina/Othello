from CountingEvaluator import CountingEvaluator
from OthelloAction import OthelloAction
from OthelloPosition import OthelloPosition
from AlphaBeta import AlphaBeta
import sys


#
# if __name__ == "__main__":
#     othello_position = sys.argv[1]
#     time_limit = sys.argv[2]
#
#     board = OthelloPosition(othello_position)
#     board.initialize()
#     counting_evaluate = CountingEvaluator()
#     alpha_beta = AlphaBeta(time_limit)
#     othello_action = alpha_beta.set_evaluator(board)
#
#     search = AlphaBeta()
#     search.set_evaluator(counting_evaluate)
#
#     # action = search.evaluator(othello_position, time_limit)
#     # action.print_move()
#
#     print("command is: python Othello.py", [othello_position], [time_limit])
#
#     print("othello action", othello_action)
#     print("alpha-beta", alpha_beta)

def main():
    if len(sys.argv) > 2:
        if len(sys.argv[1]) == 65:
            starting_position = OthelloPosition(sys.argv[1])
            time = int(sys.argv[2])

            # create minmax alpha-beta
            search = AlphaBeta()
            search.set_evaluator(CountingEvaluator())  # set evaluator

            action = search.evaluate(starting_position, time)
            action.print_move()


        else:
            print(f"Position string should be 65 chars)")
    else:
        print(f"command is: python Othello.py [position] [time]")

    if __name__ == '__main__':
        main()

    # sh.. / test_code / othellostart
    # "sh ../test_code/othello_naive" "sh ../test_code/othello_naive"
    # 5

    # sh
    # othellostart
    # "sh othello_naive" "sh ../Python/othello"
    # 5
