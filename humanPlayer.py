import player

class humanPlayer(player):
    def __init__(self, score:int, is_turn:bool)->None:
        self.score = score
        self.is_turn = is_turn

    def make_hit(self)->None:
        #Need to implement
        return