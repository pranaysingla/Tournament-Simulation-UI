from PIL import Image

img = Image.open('pp.jpg')
r, g, b = img.split()

new_img = Image.merge('RGB', (r, b, g))
new_img.show()