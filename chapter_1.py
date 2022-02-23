import cv2

#show Images
# img = cv2.imread("Resources/pikachu.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

#Show Video
cap = cv2.VideoCapture("Resources/pikachu.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break