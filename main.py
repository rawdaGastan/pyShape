from OpenGL.GL import GL_COLOR_BUFFER_BIT, glClearColor, glClear, glColor4f
from OpenGL.raw.GL.VERSION.GL_1_0 import glEnd, glVertex2f
from OpenGL.GL import glBegin, GL_LINES
import glfw

from utils.image import generate_image
from utils.init import init
from primitive.point import Point


window = init()

glfw.poll_events()
glClearColor(1, 1, 1, 1)
glClear(GL_COLOR_BUFFER_BIT)

p = Point(0, 0, width=10)
p.draw()

glfw.poll_events()

# get an image
generate_image("test", "png")

# destroy and close glfw window
glfw.destroy_window(window)
glfw.terminate()
