import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() # ret = True/False frameimage

    if not ret:
        print("Could not read frame")
        break
    cv2.imshow("Webcame Feed", frame)

    if cv2.waitKey(1) & 0xff == ord('q'): # 113 == 113 true
        print("Quitting....")
        break

cap.release()
cv2.destroyAllWindows()