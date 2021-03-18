

import matplotlib.pylab as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import scipy.ndimage as ndimage
from PIL import Image

img_file = '1.jpg'
img = plt.imread(img_file)
im = np.array(Image.open(img_file).convert('L'))

print(im.size)

thresh = 128 #to binary
maxval = 255
im_bool = (im > thresh) * maxval
gr_im = Image.fromarray(np.uint8(im_bool))
print(gr_im.size)
gr_im.show()


points = []
for i in range(100):
    points.append([np.random.uniform(0,gr_im.size[0]),np.random.uniform(0,gr_im.size[1])])
points = np.array(points)

vor = Voronoi(points)

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111)
ax.imshow(ndimage.rotate(gr_im, 180))
voronoi_plot_2d(vor, point_size=10, ax=ax)
plt.show()
