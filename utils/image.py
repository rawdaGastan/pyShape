from PIL import ImageOps, Image
from OpenGL.GL import *
from utils.constants import WIDTH, HEIGHT


def generate_image(image_name: str, extension: str):
    """
    generates an image takes the image file name
    """
    glPixelStorei(GL_PACK_ALIGNMENT, 1)

    # reads the pixels stored
    data = glReadPixels(0, 0, WIDTH, HEIGHT, GL_RGBA, GL_UNSIGNED_BYTE)

    # Creates a copy of an image memory from pixel data in a buffer
    image = Image.frombytes("RGBA", (WIDTH, HEIGHT), data)
    image = ImageOps.flip(image)

    # save the image
    image.save(image_name + "." + extension.lower(), extension.capitalize())
