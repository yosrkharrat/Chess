from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        self.squares=[[0,0,0,0,0,0,0,0] for col in range (cols)]
        self.last_move=None
        self.create()
        self.add_pieces("white")
        self.add_pieces("black")
    def move(self,piece,move):
        initial = move.initial
        final = move.final
        #concole board move update 
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece
        #move
        piece.moved = True
        #clear valid moves
        piece.clear_moves()
        #set last move 
        self.last_move=move
    def valid_move(self, piece, move):
        return move in piece.moves
    def calc_moves(self, piece, row, col):
        '''Calculate the possible moves for a piece at a given position on the board.'''
        def pawn_moves():
            #steps
            steps=1 if piece.moved else 2

            #vertical moves
            start= row + piece.dir
            end=row + piece.dir * (1+steps)
            for move_row in range(start, end, piece.dir):
                if Square.in_range(move_row):
                    if self.squares[move_row][col].isempty():
                        initial = Square(row, col)
                        final = Square(move_row, col)
                        move = Move(initial, final)
                        piece.add_move(move)
                    else:
                        break
                else:
                    break

            #diagonal moves
            move_row = row + piece.dir
            move_cols = [col - 1, col + 1]
            for move_col in move_cols:
                if Square.in_range(move_row, move_col):
                    if self.squares[move_row][move_col].has_rival_piece(piece.color):
                        initial = Square(row, col)
                        final = Square(move_row, move_col)
                        move = Move(initial, final)
                        piece.add_move(move)

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
        
        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                r, c = row + row_incr, col + col_incr
                while True:
                    if Square.in_range(r, c):
                        intial = Square(row, col)
                        final= Square(r, c)
                        move = Move(intial, final)
                        if self.squares[r][c].isempty():
                            piece.add_move(move)
                        if self.squares[r][c].has_rival_piece(piece.color):
                            piece.add_move(move)
                            break
                        if self.squares[r][c].has_team_piece(piece.color):
                            
                            break
                    else: break
                    r,c= r + row_incr, c + col_incr


        def king_moves():
            adjs=[
                (row + 1, col + 1), (row + 1, col - 1),
                (row - 1, col + 1), (row - 1, col - 1),
                (row + 1, col), (row - 1, col),
                (row, col + 1), (row, col - 1)
            ]  
            for adj in adjs:
                r, c = adj
                if Square.in_range(r, c):
                    if self.squares[r][c].isempty_or_rival(piece.color):
                        initial = Square(row, col)
                        final = Square(r, c)
                        move = Move(initial, final)
                        piece.add_move(move)       
        if isinstance(piece, Pawn):
            pawn_moves()

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            straightline_moves(
                [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            )

        elif isinstance(piece, Rook):
            straightline_moves(
                [(1, 0), (0, 1), (-1, 0), (0, -1)]
            )

        elif isinstance(piece, Queen):  
            straightline_moves(
                [(1, 1), (1, -1), (-1, 1), (-1, -1),
                 (1, 0), (0, 1), (-1, 0), (0, -1)]
            )

        elif isinstance(piece, King):
            king_moves()

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