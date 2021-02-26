import cv2

cap = cv2.VideoCapture("../Resource/DaDaDa.mp4")

#check open
if(cap.isOpened()==False):
    print("Error opening video stream or file")

while True:

    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break