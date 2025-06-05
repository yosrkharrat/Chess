import pygame
import os
from sound import Sound
from theme import Theme
class Config:
    def __init__(self):
        self.themes=[]
        self.add_themes()
        self.idx=0
        self.theme=self.themes[self.idx]
        self.font=pygame.font.SysFont('monospace',18, bold=True)
        self.move_sound=Sound(
            os.path.join("assets/sounds/move.wav")
        )
        self.capture_sound=Sound(
            os.path.join("assets/sounds/capture.wav")
        )


    def change_theme(self):
        self.idx+=1
        self.idx%= len(self.themes)
        self.theme=self.themes[self.idx]

    def add_themes(self):
        green = Theme(
            light_bg="#d0f0c0", dark_bg="#a0c0a0",
            light_trace="#c0d0c0", dark_trace="#808080",
            light_moves="#f0f0f0", dark_moves="#404040"
        )
        brown = Theme(
            light_bg="#f5deb3", dark_bg="#deb887",
            light_trace="#d2b48c", dark_trace="#8b4513",
            light_moves="#fffacd", dark_moves="#f0e68c"
        )
        blue = Theme(
            light_bg="#add8e6", dark_bg="#4682b4",
            light_trace="#b0c4de", dark_trace="#5f9ea0",
            light_moves="#e0ffff", dark_moves="#afeeee"
        )
        gray = Theme(
            light_bg="#d3d3d3", dark_bg="#a9a9a9",
            light_trace="#c0c0c0", dark_trace="#808080",
            light_moves="#f5f5f5", dark_moves="#696969"
        )
        self.themes = [green, brown, blue, gray]
 
