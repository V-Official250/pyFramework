from data.framework.window import Window
from data.framework.entity import entity
from data.framework.load import loader
from data.framework.time import Time
from data.framework.font import Font
from data.framework.animation import Animation

screen = Window(800,600,"prototype")
time = Time()
text = Font("./data/res/pixel.ttf", 16)

dirt = entity()
dirt.set_position((100,100))
texs = [loader.load_img("./data/res/dirt.png"),loader.load_img("./data/res/test.png"),loader.load_img("./data/res/download.png")]
dirt_anime = Animation(texs, 1)

while screen.isOpen:
    screen.clear(0,0,0)
    dt = time.delta
    dirt_anime.update(dt)
    dirt.texture = texs[dirt_anime.get_frame()]

    screen.render(dirt)
    screen.render_surface(text.getText(str(time.getfps()),(255,255,255)),5,5)

    screen.pollevent()
    screen.update()

    time.maxfps(60)
    time.update()