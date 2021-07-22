import pygame

#Author : V_#0343 (discord)
#data   : july 21 2021
#version: 0.0.1

class entity:
    def __init__(self) -> None:
        self.x:float = 0
        self.y:float = 0
        self.texture:pygame.Surface = pygame.Surface((0,0))

    #return entity width
    def get_width(self) -> float:
        return self.texture.get_width()

    #return entity height
    def get_height(self) -> float:
        return self.texture.get_height()

    #scale up the texture width
    def set_width(self,width:float) -> None:
        pygame.transform.scale(self.texture,(width,self.texture.get_height()))
        
    #scale up the texture height
    def set_height(self,height:float) -> None:
        pygame.transform.scale(self.texture,(self.texture.get_width(),height))
        
    #scale up the texture
    def set_size(self,width,height) -> None:
        pygame.transform.scale(self.texture,(width,height))
