from OpenGL.GL import glColor4f


class Color:
    def __init__(self, r=0, g=0, b=0, alpha=1):
        self.r = r
        self.g = g
        self.b = b
        self.alpha = alpha

    def set(self):
        glColor4f(self.r, self.g, self.b, self.alpha)
