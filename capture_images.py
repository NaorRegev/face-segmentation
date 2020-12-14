import cv2
import os

# Opens the Video file - change the name of the video.
capture_video = cv2.VideoCapture('C:/Users/naor/PycharmProjects/face_segmentation/video/lucia.mp4')
i = 0  # i for the name
count = 0  # count for limits the images for capture
path = 'C:/Users/naor/PycharmProjects/face_segmentation/capture'
while capture_video.isOpened():
    ret, frame = capture_video.read()
    if ret == False:
        break
    cv2.imwrite(os.path.join(path, str(i) + '.jpg'), frame)
    i += 1
    # waitkey= delay in milliseconds
    cv2.waitKey(5000)
    count += 1
    if count == 20:  # limits the number of images
        break

capture_video.release()
cv2.destroyAllWindows()
