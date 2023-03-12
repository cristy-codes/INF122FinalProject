from Columns.ColumnsBoard import ColumnsBoard
from Columns.ColumnsTile import ColumnsTile
from BaseGame.GameConditions import GameConditions
from BaseGame.Score import Score


class ColumnsConditions(GameConditions):
    def __init__(self, maxTime):
        super().__init__(maxTime)

    # check if there is a tile doesn't have default color in top row
    def determineGameOver(self, board: ColumnsBoard):
        for tile in board.table[0]:
            if not (tile.hasDefaultColor()):
                return True
        return False

    # drop the three queued tiles on the tile's column
    def clickEvent(self, tile: ColumnsTile, board: ColumnsBoard):
        # set tiles from queue to the top three rows in the tile's column
        swapColor(board.getTile(0, tile.col), board.column[0])
        swapColor(board.getTile(1, tile.col), board.column[1])
        swapColor(board.getTile(2, tile.col), board.column[2])
        # gravity fall column, to drop tiles to bottom
        fallColumn(board, tile.col)

    # remove matching tiles and continue drop and get points
    def pointSystem(self, score: Score, board: ColumnsBoard):
        # get points
        points, board = matchingAlgorithm(board)

        # set points
        score.addPoints(self.pointFactor(points))
        # display points
        board.scoreLabel.setText(str(score.getCurrentPoints()))  # set new score

    # each block is 50 points, times factor if more than 3
    def pointFactor(self, score: int) -> int:
        PPB = 50
        return round((1.05 ** score) * score * PPB) if (score > 3) else (score * PPB)


### HELPER functions ###

def swapColor(tileFrom: ColumnsTile, tileTo: ColumnsTile):
    temp = tileFrom.getColor()
    tileFrom.setColor(tileTo.getColor())
    tileTo.setColor(temp)


# Checks for tiles with matching colors
#   Returns points as int
def matchingAlgorithm(board: ColumnsBoard):
    points = 0
    has_fallen = True

    while has_fallen:  # if something falls, check the board again
        has_fallen = False  # nothing has fallen this run yet
        for col in range(board.get_cols()):
            # debug
            # old_row_disp = ""
            row_disp = ""
            print(board.get_rows())
            print(board.getTile(board.get_rows() - 1, col).getColor())
            # debug

            new_board = board

            # start at the bottom, work your way up
            col_range = range(board.get_rows() - 1, -1, -1)
            row_range = range(board.get_cols())

            for row in col_range:
                # old_row_disp = old_row_disp + board.getTile(row, col).getColor() + " "
                curr_board_color = board.getTile(row, col).getColor()
                print("start check: " + curr_board_color)
                print("row, col: " + str(row) + ", " + str(col))
                # check up
                if curr_board_color != "white":  # if not white
                    if row - 1 in col_range and row - 2 in col_range:  # if next two blocks in range,
                        if curr_board_color == board.getTile(row - 1,
                                                             col).getColor():  # and if tile above matches color,
                            if curr_board_color == board.getTile(row - 2,
                                                                 col).getColor():  # if 2nd above also matches color,
                                print("here!")
                                # print three before turning white
                                print(board.getTile(row, col).getColor())
                                print(board.getTile(row - 1, col).getColor())
                                print(board.getTile(row - 2, col).getColor())

                                # set scanned three to white
                                new_board.getTile(row, col).setColor("white")
                                new_board.getTile(row - 1, col).setColor("white")
                                new_board.getTile(row - 2, col).setColor("white")

                                # continues deletion
                                points, new_board = remove_up(curr_board_color, board, new_board,
                                                              range(row - 2, -1, -1), col, points)

                                # make columns fall
                                fallColumn(new_board, col)
                                has_fallen = True  # run again

                    # check right
                    if col + 1 in row_range and col + 2 in row_range:  # if next two blocks in range,
                        if curr_board_color == board.getTile(row, col + 1).getColor():  # and if right matches color,
                            if curr_board_color == board.getTile(row,
                                                                 col + 2).getColor():  # if 2nd right also matches color,
                                # set scanned three to white
                                new_board.getTile(row, col).setColor("white")
                                new_board.getTile(row, col + 1).setColor("white")
                                new_board.getTile(row, col + 2).setColor("white")

                                # make individual columns fall
                                fallColumn(new_board, col)
                                fallColumn(new_board, col + 1)
                                fallColumn(new_board, col + 2)
                                has_fallen = True  # run again

                                # continues deletion
                                points, new_board = remove_right(curr_board_color, board, new_board,
                                                                 range(col + 3, board.get_cols(), 1), row, points)

                    # check diagonals
                    if col + 1 in row_range and col + 2 in row_range:  # if next two blocks diagonally in range,
                        # diag/up
                        if row - 1 in col_range and row - 2 in col_range:  # if next two blocks diag/up in range,
                            if curr_board_color == board.getTile(row - 1,
                                                                 col + 1).getColor():  # and if diag/up matches color,
                                if curr_board_color == board.getTile(row - 2,
                                                                     col + 2).getColor():  # if 2nd diag/up also matches
                                    # set scanned three to white
                                    new_board.getTile(row, col).setColor("white")
                                    new_board.getTile(row - 1, col + 1).setColor("white")
                                    new_board.getTile(row - 2, col + 2).setColor("white")

                                    # make columns fall
                                    fallColumn(new_board, col)
                                    fallColumn(new_board, col + 1)
                                    fallColumn(new_board, col + 2)
                                    has_fallen = True  # run again

                                    remove_diagonal(curr_board_color, board, new_board,
                                                    range(col + 3, board.get_cols(), 1), row - 3, points, "UP")

                        # diag/down
                        if row + 1 in col_range and row + 2 in col_range:  # if next two blocks diag/down in range,
                            if curr_board_color == board.getTile(row + 1,
                                                                 col + 1).getColor():  # and if diag/down matches color,
                                if curr_board_color == board.getTile(row + 2,
                                                                     col + 2).getColor():  # if 2nd diag/down matches
                                    # set scanned three to white
                                    new_board.getTile(row, col).setColor("white")
                                    new_board.getTile(row + 1, col + 1).setColor("white")
                                    new_board.getTile(row + 2, col + 2).setColor("white")

                                    # make columns fall
                                    fallColumn(new_board, col)
                                    fallColumn(new_board, col + 1)
                                    fallColumn(new_board, col + 2)
                                    has_fallen = True  # run again

                                    remove_diagonal(curr_board_color, board, new_board,
                                                    range(col + 3, board.get_cols(), 1), row + 3, points, "DOWN")

                else:
                    # debug
                    print("Hit white -- ending column")
                    #
                    # if hit white, no need to continue
                    break
            print()
            # end column loop
    print("New Iteration")
    print()
    print()
    return points, board


# This method attempts deletion of a specific color looking upwards.
#   This method will end once it hits a new color
#   Returns points and new_board (updates board)
def remove_up(color: str, board: ColumnsBoard, new_board: ColumnsBoard, leftover_range: range, col: int, points: int):
    #### REPLACE with algorithm that determines how many points gained for removals ####
    MORE_THAN_THREE_POINTS = 200
    EXACTLY_THREE_POINTS = 300

    # gives points for exactly 3 removals
    points += EXACTLY_THREE_POINTS

    # start removal up
    print("start remove up")
    print(leftover_range)
    for remove_row in leftover_range:
        print("in here")
        #print("row, col: " + remove_row + " " + col + " " + board.getTile(remove_row, col).getColor())
        # if same color, continue removing
        if color == board.getTile(remove_row, col).getColor():
            print("another one")
            new_board.getTile(remove_row, col).setColor("white")
            points += MORE_THAN_THREE_POINTS
        else:
            return points, new_board  # if color doesn't match initial color, exit loop
    # end remove_row loop
    return points, new_board


def remove_right(color: str, board: ColumnsBoard, new_board: ColumnsBoard, leftover_range: range, row: int,
                 points: int):
    #### REPLACE with algorithm that determines how many points gained for removals ####
    MORE_THAN_THREE_POINTS = 200
    EXACTLY_THREE_POINTS = 300

    print("start remove right")
    # start removal right
    for remove_col in leftover_range:
        print("in here")
        print(board.getTile(row, remove_col).getColor())
        # if same color, continue removing
        if color == board.getTile(row, remove_col).getColor():
            print("another one")
            # remove & fall row
            new_board.getTile(row, remove_col).setColor("white")
            fallColumn(new_board, remove_col)
            # update points
            points += MORE_THAN_THREE_POINTS
        else:
            return points, new_board  # if color doesn't match initial color, exit loop
    # end remove_row loop
    return points, new_board


def remove_diagonal(color: str, board: ColumnsBoard, new_board: ColumnsBoard, leftover_range: range, remove_row: int,
                    points: int, diagonal_type: str):
    #### REPLACE with algorithm that determines how many points gained for removals ####
    MORE_THAN_THREE_POINTS = 200
    EXACTLY_THREE_POINTS = 300

    print("start remove diagonal")
    # Start removing diagonally. Loop is based on cols. We subtract 3 from row to account for already processed tiles
    for remove_col in leftover_range:
        print("in here")
        print(board.getTile(remove_row, remove_col).getColor())
        # if same color, continue removing
        if color == board.getTile(remove_row, remove_col).getColor():
            print("another one")
            # remove & fall row
            new_board.getTile(remove_row, remove_col).setColor("white")
            fallColumn(new_board, remove_col)

            # update points
            points += MORE_THAN_THREE_POINTS

            # iterates up if diagonal/up, iterates down if diagonal/down
            if diagonal_type.upper() == "UP":
                remove_row += 1  # increment row
            else:
                remove_row -= 1  # decrement row

        else:
            return points, new_board  # if color doesn't match initial color, exit loop
    # end remove_row loop
    return points, new_board


# Drop all tiles to bottom for one column (like gravity),
# starts from bottom (row ##), moves to top (row 0).
# Based on a sliding window algorithm, find tile that is default color (start) and tile 
# that is non-default color (stop), swap them and continue search from start
def fallColumn(board: ColumnsBoard, col: int):
    start = board.get_rows() - 1  # get bottom row
    stop = start
    # until stop is out-of-bounds, meaning that there is no more colored tiles that should be dropped
    while not stop < 0:
        # if start is not a default color tile, move both up
        if not board.getTile(start, col).hasDefaultColor():
            start -= 1  # move up
            stop -= 1  # move up
        # if stop is a default color tile, move stop up
        elif board.getTile(stop, col).hasDefaultColor():
            stop -= 1  # move up
        # both, start is a non-default color and stop is a non-default color
        else:
            swapColor(board.getTile(start, col), board.getTile(stop, col))  # swap colors
            stop = start  # reset stop, to continue drops from start
