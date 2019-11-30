#binomial theorem using pygame [link](https://www.dropbox.com/s/mdkk7u6d25r7zux/20191012_125635.mp4?dl=0)
## Installation
```SH
pip install opencv-python
pip install numpy
pip install aruco
pip install pygmae
```
## requirements
<p>prinout  4 aruco markers of 6x6 from: [create_aruco](http://chev.me/arucogen/)<br>
specify the 6x6 and number id and get printouts

import cv2
import cv2.aruco as aruco
import math
import numpy as np
from time import sleep
import pygame as pg
import sys


pg.init()

screen = pg.display.set_mode((1210,630))

## opens the camera(0-for lapcam,1-external connected webcam)

cap = cv2.VideoCapture(1)

pixel_to_cm=12.5

clock = pg.time.Clock()
#dly = pg.time.delay()
yellow = (255,255,0)
red = (255,0,0)
black = (0,0,0)
x_color = red
font = pg.font.Font(None, 32)
font1 = pg.font.Font(None, 62)


#X_square details
X_side1_box = pg.Rect(30, 15, 200, 35)
X_side2_box = pg.Rect(310, 15, 200, 35)
#Y square details
Y_side1_box = pg.Rect(600, 15, 200, 35)
Y_side2_box = pg.Rect(885, 15, 200, 35)

#X_label

#smaller square

while(True):
    for event in pg.event.get():
        if event.type == pg.QUIT:
             pg.quit(); sys.exit();
    #blanck=np.zeros((670,480,3),np.uint8)
    #out=np.zeros((630,1210,3),np.uint8)
    ret, frame1 = cap.read()
    
    
    #frame setting for play switch
    #play_frame = play_frame[1050:1190,540:605]
##    play_frame = play_frame[235:320,510:615]
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()
    
#detect aruco markers
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray,aruco_dict, parameters=parameters)
    gray = aruco.drawDetectedMarkers(gray,corners)
    rectangle = False
<p>From the centre of aruco markers line are drawn, below code finds the centre co-ordinates</p> 
```python
    try:
        screen.fill((0,0,0))
        for i in range(0,ids.size):
            if(ids[i]==1):
                    ax=int(corners[i][0][0][0])
                    ay=int(corners[i][0][0][1])
                    a1x=int(corners[i][0][2][0])
                    a1y=int(corners[i][0][2][1])
                    
                   
            elif(ids[i]==2):
                    bx=int(corners[i][0][0][0])
                    by=int(corners[i][0][0][1])
                    b1x=int(corners[i][0][2][0])
                    b1y=int(corners[i][0][2][1])
                    b2x=int(corners[i][0][1][0])
                    b2y=int(corners[i][0][1][1])
                    
            elif(ids[i]==3):
                    cx=int(corners[i][0][0][0])
                    cy=int(corners[i][0][0][1])
                    c1x=int(corners[i][0][2][0])
                    c1y=int(corners[i][0][2][1])

            elif(ids[i]==4):
                    dx=int(corners[i][0][0][0])
                    dy=int(corners[i][0][0][1])
                    d1x=int(corners[i][0][2][0])
                    d1y=int(corners[i][0][2][1])
                   
                                
        ## centre co-ordinates of 2 markers
        if 1 in ids:
            px=int((ax+a1x)/2)
            py=int((ay+a1y)/2)
            
        if 2 in ids:          
            qx=int((bx+b1x)/2)
            qy=int((by+b1y)/2)

        if 3 in ids:
            rx=int((cx+c1x)/2)
            ry=int((cy+c1y)/2)

        if 4 in ids:
            sx=int((dx+d1x)/2)
            sy=int((dy+d1y)/2)

        
    except Exception as e: pass#print(e)
 #################################################
    try:
        d=int(math.sqrt((b2y - by)**2 + (b2x - bx)**2))
        t=float(4/d)
        #when 2 markers are placed X square is drawn
        if 1 in ids and 2 in ids:
            px=int(px*2); py=int(py*2); qx=int(qx*2); qy=int(qy*2);
            X_side1 = qx - px; X_side2 = qy - py;
            
            X_side1_text = font.render('X_Square ||   X_axis: '+str(X_side1), True, (255,255,255))
            screen.blit(X_side1_text, (X_side1_box.x+5, X_side1_box.y+5))

            X_side2_text = font.render('Y_axis: '+str(X_side2), True, (255,255,255))
            screen.blit(X_side2_text, (X_side2_box.x+5, X_side2_box.y+5))
            
            
            ## drawing line in pygame
            ## right side line of x square
            pg.draw.lines(screen, yellow,False,[(px,py),(qx,py),(qx,qy)], 5)
            pg.draw.lines(screen, yellow,False,[(px,py),(px,qy),(qx,qy)], 5)
            ix=px;iy=py; jx = qx; jy = qy;

            X_label = font1.render('X', True, yellow,5)
## blit-It is a thin wrapper around a Pygame surface that allows you to easily 
## draw images to the screen
            screen.blit(X_label, (pg.Rect(qx+10,qy-int((qy-py)/2),100,32).x+5, pg.Rect(qx+10,qy-int((qy-py)/2),100,32).y+5))

            screen.blit(X_label, (pg.Rect(qx-int((qx-px)/2),qy-60,100,32).x+5, pg.Rect(qx-int((qx-px)/2),qy-60,100,32).y+5))
                
            pg.display.update()

            
            
            # when center marker os placed
            if 3 in ids and 1 in ids and 2 in ids:
                rx=int(rx*2); ry=int(ry*2);
                Y_side1 = rx - px; Y_side2 = ry - py;

                X_label = font1.render('X', True, yellow,5)
                screen.blit(X_label, (pg.Rect(qx+10,qy-int((qy-py)/2),100,32).x+5, pg.Rect(qx+10,qy-int((qy-py)/2),100,32).y+5))

                screen.blit(X_label, (pg.Rect(qx-int((qx-px)/2),qy-60,100,32).x+5, pg.Rect(qx-int((qx-px)/2),qy-60,100,32).y+5))
                    
                Y_label = font1.render('Y', True, red)
                screen.blit(Y_label, (pg.Rect(rx-int((rx-px)/2),ry+10,100,32).x+5, pg.Rect(rx-int((rx-px)/2),ry+10,100,32).y+5))
                screen.blit(Y_label, (pg.Rect(rx+10,ry-int((ry-py)/2),100,32).x+5, pg.Rect(rx+10,ry-int((ry-py)/2),100,32).y+5))
                pg.display.update()

            
                Y_side1_text = font.render('Y_Square ||    X_axis: '+str(Y_side1), True, (255,255,255))
                screen.blit(Y_side1_text, (Y_side1_box.x+5, Y_side1_box.y+5))

                Y_side2_text = font.render('Y_axis: '+str(Y_side2), True, (255,255,255))
                screen.blit(Y_side2_text, (Y_side2_box.x+5, Y_side2_box.y+5))
                
                #drawing line in pygame
                #right side line of x square
                pg.draw.lines(screen, red,False,[(px,py),(rx,py),(rx,ry)], 5)
                pg.draw.lines(screen, red,False,[(px,py),(px,ry),(rx,ry)], 5)
                ix=px;iy=py; jx = qx; jy = qy;

                pg.display.update()
                
            #play markers is seen
            if 4 in ids:
                ux = px; uy = py; vx = qx; vy = qy; wx = rx; wy = ry;
                for i in range(155):
                    screen.fill((0,0,i))
                    pg.time.delay(10)
                    pg.display.update()
                #pg.mixer.Sound.play(swoosh)
                for i in range(155,0,-1):
                    screen.fill((0,0,i))
                    pg.time.delay(10)
                    pg.display.update()
                #pg.mixer.Sound.play(swoosh)
                    
                #line draw animation
                ix = ux; iy = uy
                #half line drawn
                while ix < qx or iy < qy:
                    if ix < qx:
                        pg.draw.lines(screen, (255,255,0),False,[(px,py),(ix+5,py)], 5)
                        ix +=5
                    if iy < qy:
                        pg.draw.lines(screen, (255,255,0),False,[(px,py),(px,iy+5)], 5)
                        iy +=5;
                    pg.time.delay(35)
                    pg.display.update()
                
                
                #other half is drawn
                ix = ux; iy = uy;
                while ix < qx or iy < qy:
                    if ix < qx:
                        pg.draw.lines(screen, (255,255,0),False,[(px,qy),(ix+5,qy)], 5)
                        ix +=5
                    if iy < qy:
                        pg.draw.lines(screen, (255,255,0),False,[(qx,py),(qx,iy+5)], 5)
                        iy +=5;
                    pg.time.delay(35)
                    pg.display.update()

                 #drawing smaller square
                ix = ux; iy = uy;
                while ix < wx or iy < wy:
                    if ix < wx:
                        pg.draw.lines(screen, red,False,[(px,py),(ix+5,py)], 5)
                        ix +=5
                    if iy < wy:
                        pg.draw.lines(screen, red,False,[(px,py),(px,iy+5)], 5)
                        iy +=5;
                    pg.time.delay(35)
                    pg.display.update()
                    
                ix = ux; iy = uy;
                while ix < wx or iy < wy:
                    if ix < wx:
                        pg.draw.lines(screen, red,False,[(px,wy),(ix+5,wy)], 5)
                        ix +=5
                    if iy < wy:
                        pg.draw.lines(screen, red,False,[(wx,py),(wx,iy+5)], 5)
                        iy +=5;
                    pg.time.delay(35)
                    pg.display.update()
                    
                               
                #moving smaller sqaure and fading it out
                ix = px; iy = py; wx = rx; wy =ry;
                width = rx - px; height = ry - py;
                for i in range(4):
                    screen.fill(black)
                    
                    X_label = font1.render('X', True, yellow,5)
                    screen.blit(X_label, (pg.Rect(qx+10,qy-int((qy-py)/2),100,32).x+5, pg.Rect(qx+10,qy-int((qy-py)/2),100,32).y+5))
                    screen.blit(X_label, (pg.Rect(qx-int((qx-px)/2),qy-60,100,32).x+5, pg.Rect(qx-int((qx-px)/2),qy-60,100,32).y+5))
                    Y_label = font1.render('Y', True, red)
                    screen.blit(Y_label, (pg.Rect(rx-int((rx-px)/2),ry+10,100,32).x+5, pg.Rect(rx-int((rx-px)/2),ry+10,100,32).y+5))
                    screen.blit(Y_label, (pg.Rect(rx+10,ry-int((ry-py)/2),100,32).x+5, pg.Rect(rx+10,ry-int((ry-py)/2),100,32).y+5))
                    

                    pg.draw.lines(screen, yellow,True,[(px,qy),(qx,qy),(qx,py),(rx,py),(rx,ry),(px,ry)], 5)
                    pg.draw.rect(screen, red, pg.Rect(ix-15,iy-15,width,height), 5)
                    ix-=15; iy-=15;
                    pg.display.update()
                    pg.time.delay(600)
                    
                #fading of smaller square
                ix = px-60; iy = py - 60;
                
                while width > 5:
                    screen.fill(black)
            
                    X_label = font1.render('X', True, yellow,5)
                    screen.blit(X_label, (pg.Rect(qx+10,qy-int((qy-py)/2),100,32).x+5, pg.Rect(qx+10,qy-int((qy-py)/2),100,32).y+5))
                    screen.blit(X_label, (pg.Rect(qx-int((qx-px)/2),qy-60,100,32).x+5, pg.Rect(qx-int((qx-px)/2),qy-60,100,32).y+5))
                    Y_label = font1.render('Y', True, red)
                    screen.blit(Y_label, (pg.Rect(rx-int((rx-px)/2),ry+10,100,32).x+5, pg.Rect(rx-int((rx-px)/2),ry+10,100,32).y+5))
                    screen.blit(Y_label, (pg.Rect(rx+10,ry-int((ry-py)/2),100,32).x+5, pg.Rect(rx+10,ry-int((ry-py)/2),100,32).y+5))
                    

                    pg.draw.lines(screen, yellow,True,[(px,qy),(qx,qy),(qx,py),(rx,py),(rx,ry),(px,ry)], 5)
                    pg.draw.rect(screen, red, pg.Rect(ix,iy,width-1,height-1), 5)
                    width -=1; height-=1;
                    pg.display.update()
                    pg.time.delay(20)

                ix = rx; iy = ry; #jx =qx; jy = int(qy-(qy-ry));
                screen.fill(black)
            
                X_label = font1.render('X', True, yellow,5)
                screen.blit(X_label, (pg.Rect(qx+10,qy-int((qy-py)/2),100,32).x+5, pg.Rect(qx+10,qy-int((qy-py)/2),100,32).y+5))
                screen.blit(X_label, (pg.Rect(qx-int((qx-px)/2),qy-60,100,32).x+5, pg.Rect(qx-int((qx-px)/2),qy-60,100,32).y+5))
                Y_label = font1.render('Y', True, red)
                screen.blit(Y_label, (pg.Rect(rx-int((rx-px)/2),ry+10,100,32).x+5, pg.Rect(rx-int((rx-px)/2),ry+10,100,32).y+5))
                screen.blit(Y_label, (pg.Rect(rx+10,ry-int((ry-py)/2),100,32).x+5, pg.Rect(rx+10,ry-int((ry-py)/2),100,32).y+5))
                    


                pg.draw.lines(screen, yellow,True,[(px,qy),(qx,qy),(qx,py),(rx,py),(rx,ry),(px,ry)], 5)

                pg.display.update()

                while ix < qx:
                    pg.draw.lines(screen, red,True,[(rx,ry),(ix+2,ry)], 5)
                    ix+=2
                    pg.display.update()
                    pg.time.delay(15)
                screen.fill(black)
                #drawung yellow area
                pg.draw.rect(screen, yellow, pg.Rect(px,ry,qx-px,qy-ry), 5)

                #drawing red area
                pg.draw.rect(screen, red, pg.Rect(rx,py,qx-rx,ry-py), 5)
           
                
                screen.blit(X_label, (pg.Rect(int(qx-int((qx-px)/2)),int(qy-60),100,32).x+5, pg.Rect(qx-int((qx-px)/2),qy-60,100,32).y+5))
                X_Y_label = font1.render('(X-Y)', True, red)
                screen.blit(X_Y_label, (pg.Rect(rx+int((qx-rx)/2),py-60,100,32).x+5, pg.Rect(rx+int((qx-rx)/2),py-60,100,32).y+5))
                screen.blit(Y_label, (pg.Rect(int(qx+20),int(py+int((ry-py)/2)),100,32).x+5, pg.Rect(int(qx+20),int(py+int((ry-py)/2)),100,32).y+5))

                
                pg.display.update()
                pg.time.delay(2000)


                ix = rx
                while ix < qx:
                    #drawing red area
                    screen.fill(black)
                    #drawung yellow area
                    pg.draw.rect(screen, yellow, pg.Rect(px,ry,qx-px,qy-ry), 5)

                    screen.blit(X_label, (pg.Rect(int(qx-int((qx-px)/2)),int(qy-60),100,32).x+5, pg.Rect(qx-int((qx-px)/2),qy-60,100,32).y+5))
                    X_Y_label = font1.render('(X-Y)', True, red)
                    screen.blit(X_Y_label, (pg.Rect(rx+int((qx-rx)/2),py-60,100,32).x+5, pg.Rect(rx+int((qx-rx)/2),py-60,100,32).y+5))
                    screen.blit(Y_label, (pg.Rect(int(qx+20),int(py+int((ry-py)/2)),100,32).x+5, pg.Rect(int(qx+20),int(py+int((ry-py)/2)),100,32).y+5))

                    pg.draw.rect(screen, red, pg.Rect(int(ix+2),py,qx-rx,ry-py), 5)
                    ix+=2
                    pg.display.update()
                    pg.time.delay(15)
                    
                pg.time.delay(1000)
                #dropping the square down
                iy = py
                while iy < ry:
                    #drawing red area
                    screen.fill(black)
                    #drawung yellow area
                    pg.draw.rect(screen, yellow, pg.Rect(px,ry,qx-px,qy-ry), 5)

                    screen.blit(X_label, (pg.Rect(int(qx-int((qx-px)/2)),int(qy-60),100,32).x+5, pg.Rect(qx-int((qx-px)/2),qy-60,100,32).y+5))

                    screen.blit(X_Y_label, (pg.Rect(px-100,int(ry+((qy-ry)/2)),100,32).x+5, pg.Rect(px-100,int(ry+((qy-ry)/2)),100,32).y+5))

                    screen.blit(Y_label, (pg.Rect(int(qx+50),qy-60,100,32).x+5, pg.Rect(int(qx+50),qy-60,100,32).y+5))

                    pg.draw.rect(screen, red, pg.Rect(qx,iy+2,qx-rx,ry-py), 5)
                    iy+=2
                    pg.display.update()
                    pg.time.delay(15)

                pg.time.delay(1000)

                
                area_text = font1.render('(X2 - Y2) = (X+Y)(X-Y)', True, (255,255,255))
                screen.blit(area_text, (pg.Rect(30,30,200,50).x+5, pg.rect(30,30,200,50).y+5))
                
                pg.time.delay(3000)
                
                

                
    except Exception as e: print(e)#pass



    clock.tick(30)
    #cv2.imshow('frame',frame)
## displayes the image    
    cv2.imshow('frame',frame)
   
    
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()

