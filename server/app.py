import numpy as np
import cv2 as cv
cap = cv.VideoCapture("test_data/test.mp4")

print("Read File")
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    print(frame.shape)
    # Display the resulting frame
    if cv.waitKey(1) == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()