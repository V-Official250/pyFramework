import pygame

#Author : V_#0343 (discord)
#data   : july 20 2021
#version: 0.0.1 

class Window:
    def __init__(self, width:int, height:int, title:str):
        """working with window.using pygame."""

        #window's values
        self.width:int = width
        self.height:int = height
        self.title:str = title
        self.isOpen:bool = True

        #creating window and surface
        self.__window:pygame.display = pygame.display.set_mode((width,height))
        self.__surface:pygame.Surface = pygame.Surface((width,height)).convert_alpha()

        #setting window ti tle
        pygame.display.set_caption(title)

    #clearing window with a color (rgb)
    def clear(self,red:int,green:int,blue:int) -> None:
        self.__surface.fill((red,green,blue))

    #render a entity on to the window
    def render(self,entity) -> None:
        self.__surface.blit(entity.texture,(entity.x,entity.y))

    #render a surface or texture on to the window
    def render_surface(self,surf,x,y) -> None:
        self.__surface.blit(surf,(x,y))

    #working with the close button in window
    def pollevent(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isOpen = False

    #updating window
    def update(self) -> None:
        self.__window.blit(self.__surface,(0,0))
        pygame.display.update()