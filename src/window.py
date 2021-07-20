import pygame,sys

class Window:
    def __init__(self, width:int, height:int, title:str):
        """
        it creates a window for you application
        """

        #window's values
        self.width:int = width
        self.height:int = height
        self.title:str = title

        #setting up window and keys
        self.__window:pygame.display = pygame.display.set_mode((width,height))
        self.isOpen:bool = True

        pygame.display.set_caption(title)

    def clear(self,red:int,green:int,blue:int):
        self.__window.fill((red,green,blue))

    def pollevent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isOpen = False

    def update(self):
        pygame.display.update()
