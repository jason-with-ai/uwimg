from uwimg import *
from datetime import datetime
import shutil

# save path
save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                f"logs/tryhw0_{datetime.now().strftime('%Y-%m-%d')}")
if not os.path.exists(save_path):
    os.makedirs(save_path)
else:
    if os.path.isdir(save_path):
        shutil.rmtree(save_path)  # remove dir and all contains
        os.makedirs(save_path)
    else:
        raise ValueError("file {} is not a file or dir.".format(save_path))
        
# 1. Getting and setting pixels
im = load_image("data/dog.jpg")
for row in range(im.h):
    for col in range(im.w):
        set_pixel(im, row, col, 0, 0)
save_image(im, os.path.join(save_path,"dog_no_red"))

# 3. Grayscale image
im = load_image("data/colorbar.png")
graybar = rgb_to_grayscale(im)
save_image(graybar, os.path.join(save_path,"graybar"))

# 4. Shift Image
im = load_image("data/dog.jpg")
shift_image(im, 0, .4)
shift_image(im, 1, .4)
shift_image(im, 2, .4)
save_image(im, os.path.join(save_path,"overflow"))

# 5. Clamp Image
clamp_image(im)
save_image(im, os.path.join(save_path,"doglight_fixed"))

# 6-7. Colorspace and saturation
im = load_image("data/dog.jpg")
rgb_to_hsv(im)
shift_image(im, 1, .2)
clamp_image(im)
hsv_to_rgb(im)
save_image(im, os.path.join(save_path,"dog_saturated"))


