class Square:
    ALPHACOLS={0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.alphacol= self.ALPHACOLS[col]
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    def has_piece(self):
        return self.piece != None
    
    def isempty(self):
        return not self.has_piece() 
    
    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color
    
    def has_rival_piece(self, color):
        return self.has_piece() and self.piece.color != color
       
    def isempty_or_rival(self,color):
        return self.isempty() or self.has_rival_piece(color)
    
    @staticmethod
    def in_range(*args):
        return all(0 <= arg < 8 for arg in args)
    @staticmethod
    def get_alphacol(col):
        ALPHACOLS={0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
        return ALPHACOLS[col]
