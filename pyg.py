import pyglet
# SDL_FBDEV change is required for the Raspberry Pi PiTFT by AdaFruit
import os
os.environ["SDL_FBDEV"] = "/dev/fb1"

window = pyglet.window.Window(300,200)
image = pyglet.resource.image('umbrella.png')

@window.event
def on_draw():
        window.clear()
        image.blit(0, 0)

pyglet.app.run()
