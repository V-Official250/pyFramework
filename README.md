# pyFramework
*requires pygame 2.0+ module*

# window.py
this file contains for functions and modules for creating window and using it.
```
from window.py import Window

screen = Window(800,600,"prototype")

while screen.isOpen:
    screen.clear(255,255,255)
    screen.pollevent()
    screen.update()
```
it creates a white 800x600 window with title `prototype`.
![image](https://user-images.githubusercontent.com/85917376/126364646-2d4c3444-20f9-4c07-ba1e-f59836440475.png)
