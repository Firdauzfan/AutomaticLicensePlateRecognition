import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    cv2.circle(frame, (120, 150), 5, (0, 0, 255), -1)
    cv2.circle(frame, (530, 150), 5, (0, 0, 255), -1)
    cv2.circle(frame, (120, 340), 5, (0, 0, 255), -1)
    cv2.circle(frame, (530, 340), 5, (0, 0, 255), -1)

    pts1 = np.float32([[120, 150], [530, 150], [120, 340], [530, 340]])
    pts2 = np.float32([[100, -100], [600, -200], [-100, 150], [500, 500]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    result = cv2.warpPerspective(frame, matrix, (800, 600))


    cv2.imshow("Frame", frame)
    cv2.imshow("Perspective transformation", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
