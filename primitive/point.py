from OpenGL.GL import *
import glfw
from utils.image import generate_image
from utils.init import init
from primitive.color import Color

class Point:
    def __init__(self, x: float, y: float, color: Color, width: float = 1):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw(self):
        glLineWidth(3.0)
        glBegin(GL_POINT)
        glVertex2f(self.x, self.y)
        glEnd()

window = init()

glfw.poll_events()
glClearColor(1, 1, 1, 1)
glClear(GL_COLOR_BUFFER_BIT)

p = Point(0, 0)
p.draw()

glfw.poll_events()

#get an image 
generate_image("test", "png")

#destroy and close glfw window
glfw.destroy_window(window)
glfw.terminate()