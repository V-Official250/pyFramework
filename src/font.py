import pygame
pygame.init()

#Author : V_#0343 (discord)
#data   : july 21 2021
#version: 0.0.1

class Font:
    def __init__(self,path:str,size:int=10) -> None:
        self.font = pygame.font.Font(path,size)

    #this function return the a texture with drawn font
    def getText(self,text:str="Text",color:tuple=(0,0,0)) -> pygame.Surfaces:
        return self.font.render(text,True,color)

    #this function uninitlize the font module
    def quit(self) -> None:
        self.font.quit()
