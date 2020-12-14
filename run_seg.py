import os
import skimage.io
import matplotlib
import matplotlib.pyplot as plt
import face_seg
from PIL import Image as im
import numpy as np

# Get the number of images for detection and cropping
path, dirs, files = next(os.walk("C:/Users/naor/PycharmProjects/face_segmentation/capture"))
file_count = len(files)

for i in range(file_count):
    s1 = "c:/Users/naor/PycharmProjects/face_segmentation/capture/"
    s2 = str(i) + ".jpg"
    s3 = s1 + s2
    path = os.path.join(s3)
    # Load a image from the images folder
    image = skimage.io.imread(path)
    plt.figure(figsize=(12, 10))
    result = face_seg.remove_bkg(image)
    final = im.fromarray(result)
    final.save('result/'+str(i)+'.jpg')



