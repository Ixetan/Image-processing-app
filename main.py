from PIL import Image
image = Image.open("Овца.jpeg")

box = (0, 0, 512, 512)
region = image.crop(box)
r, g, b = region.split()
region = Image.merge("RGB", (g, b, r))
image.paste(region, box)

box = (512, 128, 1024, 600)
region = image.crop(box)
region = region.rotate(180)
r, g, b = region.split()
region = Image.merge("RGB", (g, r, b))
image.paste(region, box)

box = (128, 128, 512, 512)
region = image.crop(box)
region = region.rotate(90)
image.paste(region, box)

image.show()
