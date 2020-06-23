import numpy as np
from PIL import Image, ImageChops

# Open images
im1 = np.array(Image.open("lemur.png"))
im2 = np.array(Image.open("flag.png"))
print(im1.shape, im2.shape)
w, h, c = im1.shape
output = np.empty((w, h, c), dtype=np.uint8)
for x in range(w):
    for y in range(h):
        for z in range(c):
            output[x, y, z] = im1[x, y, z] ^ im2[x, y, z]

output = Image.fromarray(output)
output.save('output.png')
