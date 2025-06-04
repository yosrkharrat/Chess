class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
    def has_piece(self):
        return self.piece != None
    
    def iseempty(self):
        return not self.has_piece() 
    
    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color
    
    def has_rival_piece(self, color):
        return self.has_piece() and self.piece.color != color
       
    def isempty_or_rival(self,color):
        return self.iseempty() or self.has_rival_piece(color)
    
    @staticmethod
    def in_range(*args):
        return all(0 <= arg < 8 for arg in args)
