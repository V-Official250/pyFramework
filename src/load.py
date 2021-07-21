import pygame,json

#Author : V_#0343 (discord)
#data   : july 21 2021
#version: 0.0.1 

class loader():
    #this fuction loads sprite from image
    def load_sprite_fromIMG(image:pygame.Surface, x:int, y:int, width:int, height:int):
        surfacef = pygame.Surface((width,height))
        surfacef.blit(image,(x*-1,y*-1))
        return surfacef

    #this fuction loads sprite from image path
    def load_sprite_fromPATH(path:str, x:int, y:int, width:int, height:int):
        image = pygame.image.load(path)
        surfacef = pygame.Surface((width,height))
        surfacef.blit(image,(x*-1,y*-1))
        return surfacef

    #load json file and convert to enum
    def load_json(path:str):
        data = open(path, 'r').read()
        return json.loads(data)
