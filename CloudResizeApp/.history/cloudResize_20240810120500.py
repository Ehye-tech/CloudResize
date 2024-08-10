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
# cropped.show()

# resize for customized low resolution 1
# low_res_img = cropped.resize(
#     (cropped.width//4, cropped.height//4)
# )
# low_res_img.show()

# resize for customized low resolution 2
low_res_img2 = cropped.reduce(4)
# low_res_img2.show()

# make thumbnail
thumb = img.thumbnail((200,200))

low_res_img2.save("thumbnail.png", "PNG")