import cv2
import time
import sys

cap = cv2.VideoCapture(0)
directory = '.'
index = int(sys.argv[1])

while(True):
    time.sleep(0.1)
    ret, image = cap.read()
    path = directory + '/image' + '%s'%index + '.jpg'
    cv2.imwrite(path, image)
    index = index + 1
    cv2.imshow('image', image)
    print('saved ', path)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

