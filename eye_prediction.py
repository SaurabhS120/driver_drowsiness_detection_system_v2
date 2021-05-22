from keras.models import load_model
import os
import cv2
import numpy as np

lbl=['Close','Open']
model = load_model('open_close_eyes_model.h5')
path = os.getcwd()

def predict(frame,eyes):
    lbls=[]
    i=0
    prediction=[]
    for eye in eyes:
        i=i+1
        eye = cv2.resize(eye,(28,28))
        eye=eye.reshape(1,28,28,1)
        eye= eye/255
        rpred = model.predict_classes(eye)
        if(rpred[0]==1):
            lbl='Open'
        if(rpred[0]==0):
            lbl='Closed'
        prediction.append(rpred)

        #print open or closed eye on image
        # font
        font = cv2.FONT_HERSHEY_SIMPLEX

        # org
        org = (5, i*50)

        # fontScale
        fontScale = 1

        # Blue color in BGR
        color = (0, 0, 0)

        # Line thickness of 2 px
        thickness = 2

        # Using cv2.putText() method
        image = cv2.putText(frame, 'eye '+str(i)+" : "+lbl, org, font,
                            fontScale, color, thickness, cv2.LINE_AA)
    return prediction[:2]
