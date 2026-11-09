from machine import Pin
import ssd1306
import time
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

button  = Pin(15, Pin.IN, pull=Pin.PULL_UP)
button1 = Pin(14, Pin.IN, pull=Pin.PULL_UP)
button2 = Pin(16, Pin.IN, pull=Pin.PULL_UP)

j=0
k=10
m=1
m1=1
m2=1
m3=1
x = 10
y = 10
width = 8
height = 8
dx = 2
dy = 2
while True:
    oled.fill(0)   
    x += dx
    
    
  #  k=k+1
   # oled.fill_rect(60+j, 40-k*6, 4,8,1)
   # if k==50:
  #      k=0

    
    if x <=0  or x + width+32 >= 128:
        y += dy
    if x <= 0 or x + width+32 >= 128:
        dx = -dx
        
    if y==36:
        oled.text("Game Over!",30,20)
        time.sleep(3)
   # oled.fill_rect(x, y, width, height, 1)
    #if 30<x<90:

        #time.sleep(0.5)
    state2 = button2.value()
    if state2 == 0:
 #       oled.text("missile",30+j,30)
         k=k+2
    oled.fill_rect(60+j, 45-k*5, 4,8,1)

    if k==10:
         k=0
    
    if state2 == 1 + 0<k<10:
         k=k+1
        
    if x+3-3+16<60+j<x+3+3+16 +  10>k>6:
        m2=0
    if x+3-3+32<60+j<x+3+3+32 + 10>k>6:
        m3=0
    if x+3-3<60+j<x+3+3 + 10>k>6:
        m1=0
    if m1==0 + m2==0 + m3==0:
        m=0
        oled.text("Clear!",30,0)
        oled.text("Game Over!",30,20,0)
        
    oled.fill_rect(x-2,y,2,2,m1)
    oled.fill_rect(x+8,y,2,2,m1)
    oled.fill_rect(x-1,y+2,10,2,m1)
    oled.fill_rect(x-2,y+4,2,2,m1)
    oled.fill_rect(x+3,y+4,2,2,m1)
    oled.fill_rect(x+8,y+4,2,2,m1)
    oled.fill_rect(x-1,y+6,10,2,m1)
    oled.fill_rect(x-2,y+8,2,2,m1)
    oled.fill_rect(x+8,y+8,2,2,m1)
    
    oled.fill_rect(x-2+16,y,2,2,m2)
    oled.fill_rect(x+6+18,y,2,2,m2)
    oled.fill_rect(x-1+16,y+2,10,2,m2)
    oled.fill_rect(x-2+16,y+4,2,2,m2)
    oled.fill_rect(x+3+16,y+4,2,2,m2)
    oled.fill_rect(x+8+16,y+4,2,2,m2)
    oled.fill_rect(x-1+16,y+6,10,2,m2)
    oled.fill_rect(x-2+16,y+8,2,2,m2)
    oled.fill_rect(x+8+16,y+8,2,2,m2)
    
    oled.fill_rect(x-2+32,y,2,2,m3)
    oled.fill_rect(x+6+34,y,2,2,m3)
    oled.fill_rect(x-1+32,y+2,10,2,m3)
    oled.fill_rect(x-2+32,y+4,2,2,m3)
    oled.fill_rect(x+3+32,y+4,2,2,m3)
    oled.fill_rect(x+8+32,y+4,2,2,m3)
    oled.fill_rect(x-1+32,y+6,10,2,m3)
    oled.fill_rect(x-2+32,y+8,2,2,m3)
    oled.fill_rect(x+8+32,y+8,2,2,m3)
    
    state = button.value()
    if state == 0:
        j=j+8
    if j>=48:
        j=48
 
    state1 = button1.value()
    if state1 == 0:
        j=j-8
    if j<=-48:
        j=-48
        

        
    
   # oled.fill_rect(50+j,60,24,5,1) #shooter
    
    oled.fill_rect(58+j,43,8,8,1)
    oled.fill_rect(50+j,50,24,8,1)
    
    oled.show()  
    time.sleep_ms(16)	

