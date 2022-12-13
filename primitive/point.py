"""Point module"""

from OpenGL.raw.GL.VERSION.GL_1_0 import glVertex2f, glEnd, glPointSize
from OpenGL.GL import glBegin, GL_POINTS, GL_POINT_SMOOTH

from primitive.color import Color

class Point:
    """Point class"""

    def __init__(self, x: float, y: float, color: Color = Color(0, 0, 0), width: float = 1):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw(self):
        """draws a point"""
        self.color.set()

        
        glPointSize(self.width)
        glBegin(GL_POINT_SMOOTH)
        glVertex2f(self.x, self.y)
        glEnd()

