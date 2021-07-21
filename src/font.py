import pygame
pygame.init()

class Font:
    def __init__(self,path:str,size:int=10) -> None:
        self.font = pygame.font.Font(path,size)

    def getText(self,text:str="Text",color:tuple=(0,0,0)):
        return self.font.render(text,True,color)
