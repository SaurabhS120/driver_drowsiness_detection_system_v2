import cv2
def start():
    vid=cv2.VideoCapture(0)
    while(True):
        ret,frame=vid.read()
        cv2.imshow('freame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()