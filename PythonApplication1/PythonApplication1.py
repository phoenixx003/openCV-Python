from calendar import c
import cv2 as cv


img = cv.imread("C:/Users/kilic/source/repos/PythonApplication1/Screenshot (33).png")

def frameResize(frame, scale=0.5):

    x = int(frame.shape[1] * scale) #width
    y = int(frame.shape[0] * scale) #height

    return cv.resize(frame, (x, y), interpolation = cv.INTER_AREA)

#image
cv.imshow("image", frameResize(img))
#cv.waitKey(0)


#video

#vid = cv.VideoCapture("C:/Users/kilic/Downloads/WhatsApp Video 2022-08-08 at 19.57.16.mp4")
vid = cv.VideoCapture(0)

while True:

    isTrue, frame = vid.read()
    cv.flip(frame, 1, frame)

    print(isTrue)
    cv.waitKey(10)

    if cv.waitKey(10) == ord('d') or isTrue is not True:
        break

    cv.imshow("Video", frame)

vid.release()
cv.destroyAllWindows()