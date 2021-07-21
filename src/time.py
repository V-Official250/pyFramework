from typing import overload
import pygame,time

#Author : V_#0343 (discord)
#data   : july 21 2021
#version: 0.0.1

class Time:
    def __init__(self) -> None:
        self.delta:float = 0
        self.clock:pygame.time.Clock = pygame.time.Clock()
        self.__lasttime:float = time.time()

    #this function limits fps
    def maxfps(self,fps:int=60) -> None:
        self.clock.tick(fps)

    #this function return fps in readable way
    def getfps(self) -> int:
        return int(self.clock.get_fps())

    #this function return exacte fps
    def getfps_raw(self) -> float:
        return self.clock.get_fps()

    #this function update the deltatime (call only once or it wont work)
    def update(self) -> None:
        self.delta = time.time() - self.__lasttime
        self.delta *= 60
        self.__lasttime = time.time()
