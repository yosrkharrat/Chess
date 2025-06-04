import os
class Piece:
    def __init__(self, name, color,value, texture=None, texture_rect=None):
       self.name = name
       self.color = color 
       value_sign =1 if color == "white" else -1
       self.value = value*value_sign
       self.texture = texture
       self.moves=[]
       self.moved = False  # Indicates if the piece has moved
       self.texture_rect = texture_rect
       self.set_texture()
    def set_texture(self,size=80):
        self.texture=os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )
    def add_move(self, move):
        self.moves.append(move)
        
class Pawn(Piece):
    def __init__(self, color):
        if color == "white":
            self.dir=-1
        else:
            self.dir=1
        super().__init__("pawn", color, 1.0, )
class Knight(Piece):
    def __init__(self, color):
        super().__init__("knight", color, 3.0)
class Bishop(Piece):
    def __init__(self, color):
        super().__init__("bishop", color, 3.001)
class Rook(Piece):
    def __init__(self, color):
        super().__init__("rook", color, 5.0)
class Queen(Piece):
    def __init__(self, color):
        super().__init__("knight", color, 9.0)
class King(Piece):
    def __init__(self, color):
        super().__init__("king", color, 10000.0)  # King is invaluable in chess, but we assign a high value for sorting purposes