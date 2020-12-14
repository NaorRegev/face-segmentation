import os
import sys
import cv2
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image
import mrcnn.model as modellib
from mrcnn import utils
from mrcnn import visualize
import coco

# Root directory of the project
ROOT_DIR = os.path.abspath("../")
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library

# Import COCO config
sys.path.append(os.path.join(ROOT_DIR, "samples/coco/"))  # To find local version

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to trained weights file
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")
# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

# Directory of images to run detection on
IMAGE_DIR = os.path.join(ROOT_DIR, "capture")


class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


config = InferenceConfig()
config.display()

# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

# Load weights trained on MS-COCO
model.load_weights(COCO_MODEL_PATH, by_name=True)


def segment(image, predicted_image):
    idx = predicted_image['scores'].argmax()
    mask = predicted_image['masks'][:, :, idx]
    mask = np.stack((mask,) * 3, axis=-1)
    mask = mask.astype('uint8')
    bg = 255 - mask * 255
    mask_img = image * mask
    result = mask_img + bg
    return result


def remove_bkg(raw_image):
    ### implement logic
    print("Done")
    # Run detection
    result = model.detect([raw_image], verbose=0)[0]

    ##Run a segment for masking person

    mask = result['masks']
    mask = mask.astype(int)
    # mask.shape
    segmentation = segment(raw_image, result)
    result = segmentation
    return result
