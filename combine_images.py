import numpy as np
import cPickle
from PIL import Image
import os
building_dir = "building2048"
road_net_dir = "road_net2048"

print(os.path.exists(road_net_dir))
building_images = os.listdir(building_dir)
building_images.sort()
road_net_images = os.listdir(road_net_dir)
road_net_images.sort()
assert len(building_images) == len(road_net_images), "building image number is equals to road_net image number "

image_pair = zip(building_images, road_net_images)
img_size = 512
out_put = "combine"
if not os.path.exists(out_put):
    os.mkdir(out_put)
count = 0
for img_1, img_2 in image_pair:
    assert img_1 == img_2, "image file name should be equal"
    images = map(Image.open, [os.path.join(building_dir, img_1), os.path.join(road_net_dir, img_2)])
    images = [im.resize((img_size, img_size), Image.ANTIALIAS) for im in images]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB',(total_width, max_height))
    x_offet = 0

    for im in images:
        new_im.paste(im, (x_offet, 0))
        x_offet += im.size[0]

    new_im.save(os.path.join(out_put, img_1))
    count += 1
    print("process {0} images".format(count))




