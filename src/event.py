import keyboard,mouse

class Keyboard:
    def isPressed(key:str) -> bool:
        if keyboard.isPressed(key):
            return True
        else:
            return False

class Mouse:
    def getPosition():
        return mouse.get_position()

    def is_left_clicked():
        if mouse.is_pressed(button="left"):
            return True
        else:
            return False

    def is_right_clicked():
        if mouse.is_pressed(button="right"):
            return True
        else:
            return False
    
    def is_middle_clicked():
        if mouse.is_pressed(button="middle"):
            return True
        else:
            return False