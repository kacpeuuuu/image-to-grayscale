from PIL import Image

im = Image.open("image-to-grayscale/dog.jpg")
width, height = im.size

im = im.convert("RGB")

new_img = Image.new("RGB", (width, height))
src_pixels = im.load()
dst_pixels = new_img.load()

for x in range(width):
    for y in range(height):
        rgb_val = src_pixels[x,y]
        g = int(rgb_val[0]*1/3+rgb_val[1]*1/3+rgb_val[2]*1/3)
        dst_pixels[x,y] = (g,g,g)

new_img.save('grayscaled_picture.jpg')