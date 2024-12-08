from PIL import Image, ImageFilter


def open_image(filename):
    return Image.open(filename)

def blur_image(filename):
    image = Image.open(filename)
    image = image.filter(ImageFilter.GaussianBlut(2))
    image.seve(filename)

def unmask_image(filename):
    image = Image.open(filename)
    image = image.filter(ImageFilter.GaussianBlut(2))
    image.seve(filename)
