import pygame 
import sys 
from game import Game
from const import*
from move import Move
from square import Square

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
            game.show_board(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)
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
                        #validate piece color
                        if piece.color==game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            game.show_board(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                 #mouse motion    
                elif event.type==pygame.MOUSEMOTION:
                    motion_row=event.pos[1] // sqize
                    motion_col=event.pos[0] // sqize
                    game.set_hover(motion_row, motion_col)
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_board(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)
                #click release
                elif event.type==pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        released_row = dragger.mouseY // sqize
                        released_col = dragger.mouseX // sqize

                        #create possible move
                        initial=Square(dragger.initial_row, dragger.initial_col)
                        final=Square(released_row, released_col)
                        move = Move(initial, final)
                        
                        
                        #check if the move is valid
                        if board.valid_move(dragger.piece, move):
                            #normal capture
                            captured=board.squares[released_row][released_col].has_piece()
                            #move piece
                            board.move(dragger.piece, move)
                            #sounds
                            game.play_sound(captured)
                            game.show_board(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)

                            game.next_turn()

                       
                    dragger.undrag_piece()
                #key press
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        game.change_theme()
                    if event.key==pygame.K_r:
                        game.reset()
                        game=self.game
                        dragger=self.game.dragger
                        board=self.game.board

                        



                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update() 

main= Main()
main.mainloop()