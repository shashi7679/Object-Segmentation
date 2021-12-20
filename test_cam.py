import cv2

video = cv2.VideoCapture(0)

while 1:
    _,frame = video.read()

    #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    cv2.imshow("Image",frame)

    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

video.release()
cv2.destroyAllWindows()