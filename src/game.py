import pygame 
from const import *
from board import Board
from dragger import Dragger
class Game:
    def __init__(self):
        self.board=Board()
        self.dragger=Dragger()
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
                

        

