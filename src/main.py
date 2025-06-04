import pygame 
import sys 
from game import Game
from const import*


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Chess")
        self.game=Game( )

    def mainloop(self):
        game=self.game
        screen=self.screen
        dragger=self.game.dragger
        board=self.game.board
        
        while True:
            self.game.show_board(screen)
            self.game.show_moves(screen)
            self.game.show_pieces(screen)
            if dragger.dragging:
                dragger.update_blit(screen)
            for event in pygame.event.get():
                #click
                if event.type==pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    
                    clicked_row = dragger.mouseY // sqize
                    clicked_col = dragger.mouseX // sqize
                    # Check if the clicked square has a piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.calc_moves(piece, clicked_row, clicked_col)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        game.show_board(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                 #mouse motion    
                elif event.type==pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_board(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                #click release
                elif event.type==pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update() 

main= Main()
main.mainloop()