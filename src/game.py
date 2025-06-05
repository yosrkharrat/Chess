import pygame 
from const import *
from board import Board
from dragger import Dragger
class Game:
    def __init__(self):
        self.next_player='white'
        self.board=Board()
        self.dragger=Dragger()
        self.hovered_square=None
    #show methods
    def show_board(self,surface):
        for row in range(rows):
            for col in range(cols):
                if (row + col) % 2 == 0:
                    color = (234,235,200)  # white
                else:
                   color = (119,154,88)  # black
                rect = (col * sqize, row * sqize, sqize, sqize)
                pygame.draw.rect(surface, color, rect)
    def show_pieces(self,surface):  
        for row in range(rows):
            for col in range(cols):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                     #all pieces except the dragger piece
                    if piece != self.dragger.piece:
                        piece.set_texture(size=80)
                        img= pygame.image.load(piece.texture)
                        img_center=col*sqize + sqize//2, row*sqize + sqize//2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)
    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            for move in piece.moves:
                #color
                color="#B58383" if (move.final.row + move.final.col) % 2 == 0 else "#530A0A"
                #rect
                rect=(move.final.col * sqize, move.final.row * sqize, sqize, sqize)
                #blit
                pygame.draw.rect(surface, color, rect)

    def show_last_move(self, surface):
        if self.board.last_move:
            initial = self.board.last_move.initial
            final=self.board.last_move.final
            for pos in [initial, final]:
                #color
                color="#F2C94C" if (pos.row + pos.col) % 2 == 0 else "#F2994A"
                #rect
                rect=(pos.col * sqize, pos.row * sqize, sqize, sqize)
                #blit
                pygame.draw.rect(surface, color, rect)
    def show_hover(self, surface):
        if self.hovered_square:
            #color
            color="#A3A3A3" 
            #rect
            rect=(self.hovered_square.col * sqize, self.hovered_square.row * sqize, sqize, sqize)
            #blit
            pygame.draw.rect(surface, color, rect, width=3)
    def next_turn(self):
        # Logic to switch turns can be added here
        self.next_player='white' if self.next_player== 'black' else 'black'
    def set_hover(self, row, col):
        self.hovered_square= self.board.squares[row][col]
                

        

