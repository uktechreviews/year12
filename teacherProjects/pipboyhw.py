import time
from time import *
from cydr import CYD
from ili9341 import *
from xglcd_font import XglcdFont
import ntptime
from random import *
import urequests

file = open("network.info", "r", encoding="utf-8")
print ("Opened network.info")
ssid = file.readline()
ssid = ssid[:-1]
password = file.readline()
file.close()

if ssid[0]!="#":
    print ("Starting with network")
    cyd = CYD(wifi_ssid=ssid, wifi_password=password)
    state= True
else:
    print ("Starting without network SSID")
    cyd = CYD()
    state = False


vue = XglcdFont('fonts/Dejavu24x43.c', 24, 43)
uni = XglcdFont('fonts/Unispace12x24.c', 12, 24)

def setTime():
    try:
        ntptime.settime()
        print ("Time updated from ntp")
    except OSError:
        print ("Error setting the time")
        
    
def clearWeather():
    cyd.display.draw_text(0,0,"                                          ",uni, cyd.LBLACK)
    cyd.display.draw_text(0,26,"                                         ",uni, cyd.BLACK)
    cyd.display.draw_text(0,52,"                                          ",uni, cyd.DGREEN) #y value 26 for second row

def loadingAnimation(State):
    cyd.display.fill_rectangle(0, 0, 320, 240, cyd.BLACK)
    for count in range(0,10):
        cyd.display.draw_text(160,120,".",uni, cyd.GREEN)
        sleep(0.2)
        cyd.display.draw_text(160,120,"  ",uni, cyd.GREEN)
        sleep(0.2)        
    cyd.display.draw_text(0,0,"0x00000010",uni, cyd.GREEN)
    sleep(0.5)
    cyd.display.draw_text(0,0,"0x00000010  start memory",uni, cyd.GREEN)
    sleep(0.5)
    cyd.display.draw_text(0,25,"0x000000A4",uni, cyd.GREEN)
    sleep(0.5)
    cyd.display.draw_text(0,25,"0x000000A4  load memory",uni, cyd.GREEN)
    sleep(0.5)
    cyd.display.draw_text(0,50,"Memory check : .",uni, cyd.GREEN)
    sleep(0.2)
    cyd.display.draw_text(0,50,"Memory check : ..",uni, cyd.GREEN)
    sleep(0.2)
    cyd.display.draw_text(0,50,"Memory check : ...",uni, cyd.GREEN)
    sleep(0.2)
    cyd.display.draw_text(0,50,"Memory check : Passed",uni, cyd.GREEN)
    sleep(0.2)
    cyd.display.draw_text(0,75,"0x000000C9",uni, cyd.GREEN)
    sleep(0.2)
    cyd.display.draw_text(0,75,"0x000000C9  CPU0 active",uni, cyd.GREEN)
    sleep(0.2)
    cyd.display.draw_text(0,100,"0x000000D6",uni, cyd.GREEN)
    sleep(0.2)
    cyd.display.draw_text(0,100,"0x000000D6  CPU0 enabled",uni, cyd.GREEN)
    sleep(1)
    cyd.display.draw_image("image1_190x50.raw", x=50, y=140,w=190,h=50)
    sleep(2)
    cyd.display.fill_rectangle(0, 0, 320, 240, cyd.BLACK)
    for count in range(0,5):
        cyd.display.draw_text(10,0,"#",uni, cyd.GREEN)
        sleep(0.5)
        cyd.display.draw_text(10,0,"  ",uni, cyd.GREEN)
        sleep(0.5)
    cyd.display.draw_text(10,0,"** PIP-OS (R) V7.1.0.8.3 **",uni, cyd.GREEN)
    sleep(0.25)
    cyd.display.draw_text(10,25,"------------------------",uni, cyd.DGREEN)
    sleep(0.25)
    cyd.display.draw_text(10,50,"(C) 2875 ROBCO(R)", uni, cyd.GREEN)
    cyd.display.draw_text(10,75,"Loader V1.1", uni, cyd.GREEN)
    cyd.display.draw_text(10,100,"EXEC v 41.18", uni, cyd.GREEN)
    sleep(0.25)
    cyd.display.draw_text(10,125,"(C) 2875 ROBCO(R)", uni, cyd.GREEN)
    sleep(0.25)
    cyd.display.draw_text(10,150,"520KB SRAM", uni, cyd.GREEN)
    sleep(0.25)
    cyd.display.draw_text(10,175,"Dual Core: 240MHz", uni, cyd.GREEN)
    if state == False:
        cyd.display.draw_text8x8(110,232,"WIFI Error", cyd.GREEN)
        wifiIP = ""
    else:    
        wifiIP=cyd.wifi_ip()
        cyd.display.draw_text8x8(110,232,wifiIP, cyd.GREEN)
    sleep(2)
    cyd.display.fill_rectangle(0, 0, 320, 240, cyd.BLACK)
    cyd.display.draw_image("image2_133x143.raw", x=100, y=0,w=133,h=143)
    cyd.display.draw_text(10,175,"Initiating .", uni, cyd.GREEN)
    cyd.display.draw_text(10,175,"Initiating ..", uni, cyd.GREEN)
    cyd.display.draw_text(10,175,"Initiating ...", uni, cyd.GREEN)
    cyd.display.draw_text(10,175,"Initiating ....", uni, cyd.GREEN)
    sleep(0.5)
    cyd.display.draw_text(10,175,"Initiating .....", uni, cyd.GREEN)
    cyd.display.draw_text(10,175,"Initiating ......", uni, cyd.GREEN)
    cyd.display.draw_text(10,175,"Initiating .......", uni, cyd.GREEN)
    cyd.display.draw_text(10,175,"Initiating ........", uni, cyd.GREEN)
    cyd.display.draw_text(10,175,"Initiating ......... :)", uni, cyd.GREEN)
    sleep(3)
    

def getWeather():
    try:
        url = "http://api.weatherapi.com/v1/current.json?key=4f05a846856c482cb5d164806242710&q=SOLIHULL"
        r = urequests.get(url,timeout=1).json()
        print (r)
        clearWeather()
        text1 = r["current"]["condition"]["text"]
        cyd.display.draw_text(0,0,text1,uni, cyd.DGREEN)
        text2 = r["current"]["temp_c"]
        text2 = str(text2) +" oC"
        text3 = r["current"]["wind_mph"]
        text3 = "Wind "+ str(text3) + " mph"
        text4 = r["current"]["wind_dir"]
        text4 = str(text4)
        cyd.display.draw_text(240,0,text2,uni, cyd.DGREEN) 
        cyd.display.draw_text(0,26,text3,uni, cyd.DGREEN) #y value 26 for second row
        cyd.display.draw_text(240,26,text4,uni, cyd.DGREEN) #y value 26 for second row
        code = r["current"]["condition"]["code"]
        message = str(weatherMessage(code))
        cyd.display.draw_text(0,52,message,uni, cyd.DGREEN)    
    
    except OSError:
        cyd.display.draw_text(0,52,"                                          ",uni, cyd.DGREEN) #y value 26 for second row
        cyd.display.draw_text(0,52,"Weather timed out",uni, cyd.DGREEN)  
        print("timeout")
    
def weatherMessage(code):
    if code == 1000:
        return ("Have a sunny day!")
    elif code == 1009:
        return ("An overcast miserable day")
    elif code == 1030:
        return ("Watch the mist this morning")
    elif code == 1063 or code == 1150 or code == 1153 or code == 1168 or code == 1171:
        return ("You might need a raincoat")
    elif code == 1180 or code == 1183 or code == 1186 or code == 1189 or code == 1192:
        return ("You need a raincoat")
    elif code == 1195:
        return ("Warning: Very wet")
    elif code == 1066:
        return ("**** SNOW WARNING! ****")
    elif code == 1069 or code == 1072:
        return ("Take extra care driving")
    elif code == 1087:
        return ("Thunder storms - take care")
    elif code == 1114 or code == 1117:
        return ("Do not leave the house!")
    elif code == 1135 or code == 1147:
        return ("Fog lights needed")
    elif code == 1114 or code == 1117:
        return ("Do not leave the house!")
    elif code == 1210 or code == 1213 or code == 1216 or code == 1219 or code == 1222 or code == 1225:
        return ("Snow warning, take care!")
    else:
        return ("")


def updateClock(posX,posY):
    actual_time=gmtime()
    mins = actual_time[4]
    if mins <=9:
        mins = "0"+str(actual_time[4])
    hours = actual_time[3]
    if hours <=9:
        hours = "0"+str(actual_time[3])
    timeDisplay = str(hours)+" "+str(mins) + ""
    date = (str(actual_time[2]) + "/" + str(actual_time[1])  + "/" + str(actual_time[0])+ "")
    cyd.display.draw_text(posX,posY+20,timeDisplay,vue, cyd.BLACK,background=cyd.DGREEN)
    cyd.display.draw_text(10,150,date,uni, cyd.BLACK,background=cyd.DGREEN)
   
def cleanUp(posX,posY):
    cyd.display.draw_text(posX,posY+15,"      ",vue, cyd.DGREEN,background=cyd.DGREEN)  #clean up time
    cyd.display.draw_text(10,150,"     ",uni, cyd.DGREEN,background=cyd.DGREEN) #cleanup date
    
def pauseTime(posX,posY,seconds):
    for i in range (0,seconds):
        x, y = cyd.touches()
        if x != 0 and y != 0:
            print ("Screen pressed")
            global flag
            flag = True
            break
        cyd.display.draw_text(posX+50,posY+15,":",vue, cyd.GREEN,background=cyd.DGREEN)
        images = ["#","  "]
        for image in images:
            cyd.display.draw_text(305,215,image,uni,cyd.GREEN)
            sleep(0.55)
        cyd.display.draw_text(posX+50,posY+15," ",vue, cyd.GREEN,background=cyd.DGREEN)
        for image in images:
            cyd.display.draw_text(305,215,image,uni,cyd.GREEN)
            sleep(0.55)
         
def setUpScreen(Welcome):
    cyd.backlight(1)
    if Welcome == True:
        loadingAnimation(state)
    cyd.display.draw_image("bg2.raw", x=0, y=0,w=320,h=240)
    cyd.display.fill_rectangle(10, 90, 150, 95, cyd.DGREEN)
    cyd.display.draw_text8x8(0,232,"ROBCO INDUSTRIES", cyd.GREEN)
    

def wifiStatus():
    wifiStatus=cyd.wifi_isconnected()                          # Checks to see that the wifi connection is connected.
    wifiIP=cyd.wifi_ip()
    cyd.display.draw_text8x8(140,232,wifiIP, cyd.GREEN)
    if wifiStatus == True:
        network = "WiFi"
        cyd.display.draw_text8x8(140,232,wifiIP, cyd.GREEN)
    else:
        network = "Error"
        cyd.display.draw_text8x8(140,232,"           ", cyd.GREEN)
    cyd.display.draw_text8x8(278,82,network, cyd.DGREEN)
    
setTime() # updates time and traps if no wifi 

flag = False

setUpScreen(True) # Set to False to avoid loading animation

while True:
    if flag!=True:
        getWeather()
        try:
            wifiStatus()
        except AttributeError:
            print ("Can't connect to WIFI")
        for count in range (1,20): #change this value to update the weathr more frequently
            print (count)
            if flag == True:
                break
            x = 10
            y = 80
            updateClock(x,y)  
            pauseTime(x,y,10) #change this value to update the clock time more frequently
            cleanUp(x,y)
    else:
        while True:
            cyd.display.fill_rectangle(0, 0, 320, 240, cyd.BLACK)
            cyd.display.draw_image("image2_133x143.raw", x=randint(0,180), y=randint(0,85),w=133,h=143)
            x, y = cyd.touches()
            if x != 0 and y != 0:
                print ("Screen pressed")
                flag = not flag
                setUpScreen(False)
                break
            sleep(1)
        sleep(1)

