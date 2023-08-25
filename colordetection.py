import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1288)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,729)

#To get centre divide by height and divide by width


while True:
   channel, frame = cap.read()
   hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#compare the color in frame
   height, width, channel = frame.shape
   cx = int(width / 2)
   cy = int(height / 2)
   #pick pixel value
   pixel_center=hsv_frame[cy,cx] #picking pixel value fron hsv frame
   hue_value = pixel_center[0] #to take only h value
   color = "Undefined"
   if hue_value < 5:
      color = "RED"
   elif hue_value < 22:
      color = "ORANGE"
   elif hue_value < 33:
      color = "YELLOW"
   elif hue_value < 78:
      color = "GREEN"
   elif hue_value < 131:
      color = "BLUE"
   elif hue_value < 170:
      color = "VIOLET"
   else:
      color = "RED"

   pixel_center_bgr = hsv_frame[cy,cx]
   b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
   cv2.putText(frame, color, (10, 70), 0, 1.5,(b, g, r),2 )
   cv2.circle(frame,(cx,cy),5,(25,25,35),3)


   cv2.imshow("Frame",frame)
   key=cv2.waitKey(1)
   if key == 27:
      break

cap.release()
cv2.destroyAllwindows()

