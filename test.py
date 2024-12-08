from PIL import Image, ImageFilter

image = image.open(Овца.jpeg)
image = image.filter(ImageFilter.GaussianBlur(10))

image.show()