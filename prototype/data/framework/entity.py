import pygame

#Author : V_#0343 (discord)
#data   : july 21 2021
#version: 0.0.1

class entity:
    def __init__(self) -> None:
        self.x:float = 0
        self.y:float = 0
        self.texture = pygame.Surface((0,0))

    #return (x,y) as tuple
    def get_position(self) -> tuple:
        return (self.x,self.y)

    #set position x,y by tuple (x,y)
    def set_position(self,pos:tuple) -> None:
        self.x = pos[0]
        self.y = pos[1]

    #return tuple of width and height
    def get_size(self):
        return (self.texture.get_width(),self.texture.get_height())

    #set texture to the entity
    def set_texture(self, texture) -> None:
        self.texture = texture    

    #set size by tuple (width, height)
    def set_size(self,size:tuple) -> None:
        pygame.transform.scale(self.texture,(size[0],size[1]))

    #return entity width
    def get_width(self) -> float:
        return self.texture.get_width()

    #return entity height
    def get_height(self) -> float:
        return self.texture.get_height()