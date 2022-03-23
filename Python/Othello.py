from cgi import log

sequence=None
import os
import strconv


def __main__() :
    string sequence
    int time

    # // error handling
    if len(os.Args) > 1 :
        sequence = os.Args[1];
    else :
        log.Fatal("No string was given");
    if len(os.Args) > 2 :
        time, _ = strconv.Atoi(os.Args[2]);
    else :
        log.Fatal("No timeout given");

    if len(sequence) != 65 :
        log.Fatal("The string has to be of size 65");

    #
    # // Parse the string board, format it and look for the best playable move according to heuristic
    currentBoard == NewBoard();

    currentBoard.OthelloPosition(sequence);
    abp == NewAlphaBetaPruning(time);

    move == abp.Evaluate(currentBoard);
    if move == Null:
        log.Fatal("The program timeout without being able to result any move");
    print(move)
