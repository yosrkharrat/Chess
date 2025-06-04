from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        self.squares=[[0,0,0,0,0,0,0,0] for col in range (cols)]

        self.create()
        self.add_pieces("white")
        self.add_pieces("black")
    def calc_moves(self, piece, row, col):
        '''Calculate the possible moves for a piece at a given position on the board.'''
        def knight_moves():
            possible_moves = [
                
                (row + 2, col + 1), (row + 2, col - 1),
                (row - 2, col + 1), (row - 2, col - 1),
                (row + 1, col + 2), (row + 1, col - 2),
                (row - 1, col + 2), (row - 1, col - 2)

            ]
            for possible_move in possible_moves:
                r,c= possible_move
                if Square.in_range(r, c):
                    if self.squares[r][c].isempty_or_rival(piece.color):
                        initial=Square(row,col)
                        final=Square(r,c) 
                        move=Move(initial, final)
                        piece.add_move(move)

        if isinstance(piece, Pawn):
            pass
        elif isinstance(piece, Knight):
            knight_moves()
        elif isinstance(piece, Bishop):
            pass 
        elif isinstance(piece, Rook):
            pass
        elif isinstance(piece, Queen):  
            pass
        elif isinstance(piece, King):
            pass
    def create (self):
        
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row, col)
    def add_pieces(self, color):
        if color == "white":
            row_pawn, row_other = (6, 7)
        else:
            row_pawn, row_other = (1, 0)
        # Pawns
        for col in range(cols):
            self.squares[row_pawn][col]=Square(row_pawn,col,Pawn(color)) 
        #knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))