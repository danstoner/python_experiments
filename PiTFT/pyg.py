import pyglet

window = pyglet.window.Window(300,200)
image = pyglet.resource.image('umbrella.png')

@window.event
def on_draw():
        window.clear()
        image.blit(0, 0)

pyglet.app.run()
