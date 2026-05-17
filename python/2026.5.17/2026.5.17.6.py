from PIL import Image

im = Image.open("XP.JPG")
im = im.convert("L")
im = im.point(lambda x: 255 if x > 127 else 0)
im.save("New_XP.JPG", "JPEG")