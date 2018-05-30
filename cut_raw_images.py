from PIL import Image
import os

im = Image.open("raw_images/road_net.jpg")
width, height = im.size
print("width:{0}, height:{1}".format(width, height))

crop_size = 2048
stride = crop_size // 2
w_size = (width - crop_size) // stride + 1
h_size = (height - crop_size) // stride + 1
output_dir = "road_net" + str(crop_size)
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
count = 0
for i in range(w_size):
    for j in range(h_size):
        count += 1
        im.crop((i * stride, j * stride,  i * stride + crop_size, j * stride + crop_size)).save(os.path.join(output_dir, str(crop_size) + str(count) + ".jpg"))
        print("get {0} images".format(count))
