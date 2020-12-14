# face-segmentation
Face segmentation using Mask_RCNN model

The final result is images of a person, without any background. Only the person itself with a white background. These images are great for machine learning models. 

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

example:
capture images from a video:
![15](https://user-images.githubusercontent.com/71181322/102065532-56f94c00-3e01-11eb-9098-3fb48b2343db.jpg)
![0](https://user-images.githubusercontent.com/71181322/102065537-582a7900-3e01-11eb-8499-a78786457d59.jpg)
![0](https://user-images.githubusercontent.com/71181322/102067503-da1ba180-3e03-11eb-9044-3be875e73473.jpg)

The results:
![15](https://user-images.githubusercontent.com/71181322/102065552-5fea1d80-3e01-11eb-9822-a59a25bd2539.jpg)
![0](https://user-images.githubusercontent.com/71181322/102065554-611b4a80-3e01-11eb-8ab4-adf36bac3d44.jpg)
![0](https://user-images.githubusercontent.com/71181322/102067514-ddaf2880-3e03-11eb-99ef-5c7fdd9a5581.jpg)



