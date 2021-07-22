# pyFramework
*requires pygame 2.0+ module*

# simple window
this files contains for functions and modules for creating window and rendering textures or shapes.
```
from window import Window

win = Window(800,600,"prototype")

while win.isOpen:
    win.clear(255,255,255)
    win.pollevent()
    win.update()
```
it creates a white 800x600 window with title `prototype`.
![image](https://user-images.githubusercontent.com/85917376/126364646-2d4c3444-20f9-4c07-ba1e-f59836440475.png)

# Rendering image
to render image you have to must clear window `win.clear(0,0,0)`
```
from window import Window
from entity import entity
from load import loader

win = Window(800,600,"prototype")
img = entity()
img.x = 100
img.y = 100
img.texture = loader.load_img("./path/to/img")

while win.isOpen:
    win.clear(0,0,0)
    win.render(texture)
    win.pollevent()
    win.update()
```
this will create a window with a rendering img
