import cv2
import eye_prediction
import sound
import progess_bar
CLOSED_EYE=0
eye_cascade=cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
want_continue=True
def findEyes(frame):
    eyes_coords=eye_cascade.detectMultiScale(frame)
    eyes=[]
    n=0
    for x,y,w,h in eyes_coords:
        n=n+1
        #draw dectangle on eyes
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),1)
        #crop eyes only 2
        if n<=2:
            eye=frame[y:y+h,x:x+w]
            eye=cv2.resize(eye,(24,24))
            eyes.append(eye)
        else:
            break
    return frame,eyes
def start():
    print("opening camera")
    vid=cv2.VideoCapture(0)
    count=0

    while(want_continue):
        ret,frame=vid.read()
        # convert color image to gray scale image(B&W)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray,eyes=findEyes(gray)
        prediction=eye_prediction.predict(gray,eyes)
        i=0
        if len(prediction)>=2:
            if prediction[0]==CLOSED_EYE and prediction[1]==CLOSED_EYE:
                count=count+1
            else:
                if count>0:
                    count=count-0.5
        if count > 10:
            sound.alert()
            count=0
        #for eye in eyes:
        #    i=i+1
        #    cv2.imshow("eye"+str(i),eye)
        cv2.imshow('Drowsiness detection',gray)
        cv2.moveWindow("Drowsiness detection",10,10)
        progess_bar.update(count)

    vid.release()
    progess_bar.close()
    cv2.destroyAllWindows()