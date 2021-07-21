import pygame

class entity:
    def __init__(self, texture:pygame.Surface, x:float, y:float, width:float, height:float) -> None:
        self.rect = pygame.Rect(x,y,width,height)
        self.texture = texture
