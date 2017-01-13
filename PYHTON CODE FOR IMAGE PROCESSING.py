#======================IMPORTING LIBRARIES=============
import numpy as np 	#Importing 'numpy' library for computing
import cv2		#Importing library for OpenCV
import serial  		#Importing library for PySerial

#==========================BAUD RATE =================
ser = serial.Serial('COM3',9600)   #baud rate on the communication port 'COM3'.

a = 0
b = 0
frame_no=0
y = 0
z = 0

#==========================TRANSITION TIME ============
cap = cv2.VideoCapture(2)    #capturing the video from the attached external camera or the internally buil webcam built. The paramenter for the former is 2 and that for the latter is 1.
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()  #reading each frame one by one.
    #print ret 
    frame_no=frame_no+1  # counter to calculate no. of frames. Increments each time a new frame is read from the camera.
    if frame_no==2:
        break        #This short operation was for the frame to settle first. 

#=======================COLOR DETECTION AND CONTOUR MAKING======================

while(True):    #infinity loop
    ret, frame = cap.read()
    #-------CALIBRATION----------------
    # The operations on the frame come here.
    
    #defining color range
    #Values for callibration to be put here.
    ball_MIN = np.array([15, 15, 35])   #minimum RGB value found of all the values found of all the points falling in the ball's region
    ball_MAX = np.array([40, 45, 110])  #maximum RGB value found of all the values found of all the points falling in the ball's region
    BOT_MIN = np.array([180, 180, 180]) #minimum RGB value found of all the values found of all the points falling in the bot's region
    BOT_MAX = np.array([255, 255, 255]  #minimum RGB value found of all the values found of all the points falling in the bot's region

    
    # ------MASKING---------------------
    mask1 = cv2.inRange(frame, ball_MIN, ball_MAX)   # a numpy array is created of all the pixels whoses RGB values lie in the given range.
    mask2 = cv2.inRange(frame, BOT_MIN, BOT_MAX)
    
    #to find contours and centre of ball
    #--------DRAWING CONTOURS AND CENTROID-----
    contours_ball, hierarchy = cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # this function #findcontours function draws contours of 'mask1' here. Second parameter is the hierarchy retreival mode chosen viz. is not relevant in this case. Third parameter is the approximation method employed for drawing contours.
    for i in range(len(contours_ball)):
        if cv2.contourArea(contours_ball[i]) > 1 and cv2.contourArea(contours_ball[i]) < 50000:   #This is basically to eliminate all the small areas (lying in the given RGB range) being captured unnecessarily due to lighting conditions
            cv2.drawContours(frame,contours_ball[i],-1,(0,255,0),2)     #First parameter is the source window; second are the contour list passed as a python numpy array list; third is colour, fourth is thickness. 
            M1 = cv2.moments(contours_ball[i])		#formula for finding the centroid of the ball
            a =int(M1['m10']/M1['m00'])			#x coordinate of the centroid
            y =int(M1['m01']/M1['m00'])  		#y coordinate of the centroid
            cv2.circle(frame,(a,y), 3, (0,255,0), -1)#why 3   #plotting a circle in the window 'frame'; having its centre at (a,y); radius 3 pixels, colour green, -1 implies that the closed image filled.
                            
    #to find contour and centre of box (similar)

    contours_BOT, hierarchy = cv2.findContours(mask2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours_BOT)):
        if cv2.contourArea(contours_BOT[i]) > 500 and cv2.contourArea(contours_BOT[i]) < 20000000000:
            cv2.drawContours(frame,contours_BOT[i],-1,(0,0,255),2)
            M2 = cv2.moments(contours_BOT[i]) 
            b =int(M2['m10']/M2['m00'])
            z =int(M2['m01']/M2['m00'])
            cv2.circle(frame,(b,z), 3, (0,0,255), -1)      

# ====================== TRANSLATION OF THE BOT TO CATCH THE BALL=============                              
#  to direct the motor whether to translate left or right or remain in its position
# here PySerial communicates with Arduino IDE and send the corresponding character
   
    if (y - z > 0) :
        ser.write('R')   
    elif (y - z < 0) :
        ser.write('L')
    else:
        ser.write('N')
    cv2.imshow('frame', frame)
    k = cv2.waitKey(0) & 0xff       
    if k == 27: break               #the program stops running if esc key is pressed.
    frame_no=frame_no+1
    
cap.release()      
cv2.destroyAllWindows()   #close everything
