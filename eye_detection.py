import cv2
import eye_prediction
import sound
eye_cascade=cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
def findEyes(frame):
    eyes_coords=eye_cascade.detectMultiScale(frame)
    eyes=[]
    for x,y,w,h in eyes_coords:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),1)
        eye=frame[y:y+h,x:x+w]
        eye=cv2.resize(eye,(24,24))
        eyes.append(eye)
    return frame,eyes

def start():
    vid=cv2.VideoCapture(0)
    count=0
    while(True):
        ret,frame=vid.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray,eyes=findEyes(gray)
        prediction=eye_prediction.predict(gray,eyes)
        cv2.imshow('freame',gray)
        i=0
        if len(prediction)>=2:
            if prediction[0]==0 and prediction[1]==0:
                count=count+1
            else:
                count=0
        if count > 10:
            sound.alert()
            count=0
        for eye in eyes:
            i=i+1
            cv2.imshow("eye"+str(i),eye)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        print("count: "+str(count))
    vid.release()