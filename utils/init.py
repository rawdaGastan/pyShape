import glfw

from utils.constants import WIDTH, HEIGHT, TITLE

def init():
    """
    Start a new glfw window to draw
    """
    if not glfw.init():
        return

    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)

    window = glfw.create_window(WIDTH, HEIGHT, TITLE, None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    return window
