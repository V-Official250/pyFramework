from typing import overload
import pygame,time

class Time:
    def __init__(self) -> None:
        self.delta:float = 0
        self.lasttime:float = time.time()
        self.clock:pygame.time.Clock = pygame.time.Clock()

    def maxfps(self,fps:int=60) -> None:
        self.clock.tick(fps)

    def getfps(self) -> int:
        return int(self.clock.get_fps())

    def getfps_raw(self) -> float:
        return self.clock.get_fps()

    def update(self) -> None:
        self.delta = time.time() - self.lasttime
        self.delta *= 60
        self.lasttime = time.time()
