from PIL import Image
filename = "buildings.jpg"
with Image.open(filename) as img:
    img.load()
type(img)
# regenerate imgs
# img.show()

# for logs
# print(isinstance(img, Image.Image))
# img.format
# img.size
# img.mode


# extract one building from all buildings
cropped = img.crop((300,50,700,1000))
cropped.show()