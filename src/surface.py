import pygame

class Surface:
    def create(width:int, height:int):
        return pygame.Surface((width,height))

    def resize(surface:pygame.Surface,width:int,height:int):
        return pygame.transform.scale(surface,(width,height))

    def rotate(surface:pygame.Surface,angle):
        return pygame.transform.rotate(surface,angle)

    def flip(surface:pygame.Surface,xbool:bool,ybool:bool):
        return pygame.transform.flip(surface,xbool,ybool)

    def crop(surface:pygame.Surface,x,y,width,height):
        surfacef = pygame.Surface((width,height))
        surfacef.blit(surface,(x*-1,y*-1))
        return surfacef