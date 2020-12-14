# face-segmentation
Face segmentation using Mask_RCNN model

The segmentation work in few steps:
1. Make a folder called "capture", a folder called "video", and a folder called "result". 
2. If you want to make images from a video - download the video to the "video" folder, and run the capture_images python file.
3. if you want to make images without background from exists images - copy your images to the "capture" folder.
4. Run the run_seg python file.
5. All your images after the face segmentation will be saved into the "result" folder.

There are three main files:

1. capture_images:
This python file is to capture images from a video from the "video" library in your folder.
parameters to change in the code:
video location to be captured.
waitkey - delay in milliseconds between frames captured from the video.
count - how many images to be captured.

2. face_seg:
This python file is the main code for the face segmentation.
parameters to change in the code:
ROOT_DIR
COCO_MODEL_PATH - the location where "mask_rcnn_coco.h5" is saved.
if you don't download this file, it will be automatically downloaded. 

3. run_seg:
This python file is the main run for the face segmentation.
I use these codes to save the images after the segmentation and remove the background.
You can also do anything you want with the 'result' image.


