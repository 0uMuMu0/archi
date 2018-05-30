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
    building = Image.open(os.path.join(building_dir, img_1)).resize((img_size, img_size), Image.ANTIALIAS)
    road_net = Image.open(os.path.join(road_net_dir, img_2)).resize((img_size, img_size), Image.ANTIALIAS)
    X_im = Image.new('RGB', (img_size, img_size))

    top_build = building.crop((0, 0, img_size, img_size/4))  # left, upper, right, lower
    X_im.paste(top_build, (0, 0, img_size, img_size/4))

    left_build = building.crop((0, img_size/4, img_size/4, img_size*3/4))
    X_im.paste(left_build, (0, img_size/4, img_size/4, img_size*3/4))

    right_build = building.crop((img_size*3/4, img_size/4, img_size, img_size*3/4))
    X_im.paste(right_build, (img_size*3/4, img_size/4, img_size, img_size*3/4))

    bottom_build = building.crop((0, img_size*3/4, img_size, img_size))
    X_im.paste(bottom_build, (0, img_size*3/4, img_size, img_size))

    center_road_net = road_net.crop((img_size/4, img_size/4, img_size*3/4, img_size*3/4))
    X_im.paste(center_road_net, (img_size/4, img_size/4, img_size*3/4, img_size*3/4))

    combine_im = Image.new('RGB', (2*img_size, img_size))
    combine_im.paste(building, (0, 0))
    combine_im.paste(X_im, (img_size, 0))

    combine_im.save(os.path.join(out_put, img_1))
    count += 1
    print("process {0} images".format(count))




