import player

class computerPlayer(player):
    def __init__(self, score:int, is_turn:bool)->None:
        self.score = score
        self.is_turn = False

    def make_hit(self)->None:
        #Need to implement
        return