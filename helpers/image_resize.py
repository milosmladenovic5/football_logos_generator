import os
from scipy.misc import imread, imsave, imresize

src = "../data/original_data" # original data
dst = "../data/resized_data_128" # resized

os.mkdir(dst)

for each in os.listdir(src):
    img = imread(os.path.join(src,each))
    img = imresize(img,(128,128))
    imsave(os.path.join(dst,each), img)
    