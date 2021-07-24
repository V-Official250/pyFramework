import pygame

class Animation:
    def __init__(self, frames:list, speed:float) -> None:
        self.frames:list = frames
        self.speed:float = speed
        self.frame:float = 0

    #this fuction updates to the net frame if the time is over
    def update(self, delta:float=1) -> None:
        if self.frame >= (len(self.frames)- self.speed):
            self.frame = 0
        else:
            self.frame += self.speed * delta

    def get_frame(self) -> int:
        while self.frame > len(self.frames):
            if self.frame >= len(self.frames):
                self.frame -= self.frame - len(self.frames)
        return int(self.frame-self.speed)
