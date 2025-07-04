import pygame 
from const import *
from board import Board
from dragger import Dragger
from config import Config
from square import Square
class Game:
    def __init__(self):
        self.next_player='white'
        self.board=Board()
        self.dragger=Dragger()
        self.hovered_square=None
        self.config=Config()
    #show methods
    def show_board(self,surface):
        theme=self.config.theme
        for row in range(rows):
            for col in range(cols):
                #color
                color=theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                #rect
                rect = (col * sqize, row * sqize, sqize, sqize)
                #blit   
                pygame.draw.rect(surface, color, rect)
                #row coordinate
                if col == 0:
                    color=theme.bg.dark if row % 2 == 0 else theme.bg.light
                    lbl=self.config.font.render(str(rows-row), 1, color)
                    lbl_pos=(5,5+row*sqize)
                    surface.blit(lbl, lbl_pos)
                #col coordinate
                if row == rows - 1:
                    color=theme.bg.dark if (col+row) % 2 == 0 else theme.bg.light
                    lbl=self.config.font.render(Square.get_alphacol(col), 1, color)
                    lbl_pos=(col*sqize + sqize-20, height - 20)
                    surface.blit(lbl, lbl_pos)


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
        theme=self.config.theme
        if self.dragger.dragging:
            piece = self.dragger.piece
            for move in piece.moves:
                #color
                color=theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                #rect
                rect=(move.final.col * sqize, move.final.row * sqize, sqize, sqize)
                #blit
                pygame.draw.rect(surface, color, rect)

    def show_last_move(self, surface):
        theme=self.config.theme
        if self.board.last_move:
            initial = self.board.last_move.initial
            final=self.board.last_move.final
            for pos in [initial, final]:
                #color
                color=theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
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
    def change_theme(self):
        self.config.change_theme()
    def play_sound(self, captured=False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()
    def reset(self):
        self.__init__()


        

