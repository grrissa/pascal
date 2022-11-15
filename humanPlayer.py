import player, gameboard, cell

class humanPlayer(player):
    def __init__(self, score:int, is_turn:bool, board:cell[][])->None:
        self.score = score
        self.is_turn = is_turn
        self.board = board

    def make_hit(self)->None:
        #Need to implement
        return