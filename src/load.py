import pygame

class loader():
    def load_sprite_fromIMG(image:pygame.Surface, x:int, y:int, width:int, height:int):
        surfacef = pygame.Surface((width,height))
        surfacef.blit(image,(x*-1,y*-1))
        return surfacef

    def load_sprite_fromPATH(path:str, x:int, y:int, width:int, height:int):
        image = pygame.image.load(path)
        surfacef = pygame.Surface((width,height))
        surfacef.blit(image,(x*-1,y*-1))
        return surfacef
