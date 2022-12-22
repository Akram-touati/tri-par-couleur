import csv
import RPi.GPIO as GPIO
import time




GPIO.setmode(GPIO.BOARD)
print("initialisation des servomoteurs")
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

servo1 = GPIO.PWM(11,50)
servo1.start(0)

servo2 = GPIO.PWM(12,50)
servo2.start(0)

time.sleep(2)
duty=2


#initialisation servo2 (90°)
# servo2.ChangeDutyCycle(5)
# time.sleep(0.3)
# servo2.ChangeDutyCycle(0)
# time.sleep(0.5)




while True:
    #initialisation servo1 (0°)
    servo1.ChangeDutyCycle(11.5)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    print("servo1 récupére le produit 0°")
    time.sleep(2)

    
    print("servo1 vers caméra")
    
    servo1.ChangeDutyCycle(8)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    print("Detection en cours")
    time.sleep(2)
    
    
    with open('/home/pi/Desktop/Anis/pythonProject1/myCSVfile.csv', mode='r') as x:
        x = csv.reader(x, delimiter=',')
        for y in x:
            if y[0] == "m":
                print("rotation du servo2 vers le bac maron vers bac maron 90°")
                servo2.ChangeDutyCycle(7)
                time.sleep(0.3)
                servo2.ChangeDutyCycle(0)
                time.sleep(2)
                print("rotation du servo1 vers la tige")
                servo1.ChangeDutyCycle(6.7)
                time.sleep(0.3)
                servo1.ChangeDutyCycle(0)
                time.sleep(2)
                print ("servo1 90°")
#             if y[0] == "v":
#                 print("rotating vers bac vert 40°" )
#                 servo2.ChangeDutyCycle(4)
#                 time.sleep(0.3)
#                 servo2.ChangeDutyCycle(0)
#                 print("servo2 vers bac vert")
#                 time.sleep(0.5)
#                 servo1.ChangeDutyCycle(7.6)
#                 time.sleep(0.3)
#                 servo1.ChangeDutyCycle(0)
#                 time.sleep(1)
#                 print ("servo1 90°")
            if y[0] == "b":
                print("rotation du servo2 vers le bac bleu vers bac maron 36°")
                servo2.ChangeDutyCycle(4)
                time.sleep(0.3)
                servo2.ChangeDutyCycle(0)
                time.sleep(2)
                print("rotation du servo1 vers la tige")
                servo1.ChangeDutyCycle(6.7)
                time.sleep(0.3)
                servo1.ChangeDutyCycle(0)
                time.sleep(2)
                print ("servo1 90°")
            if y[0] == "r":
                print("rotation du servo2 vers le bac rouge vers bac maron 0°")
                servo2.ChangeDutyCycle(2)
                time.sleep(0.3)
                servo2.ChangeDutyCycle(0)
                time.sleep(2)
                print("rotation du servo1 vers la tige")
                servo1.ChangeDutyCycle(6.7)
                time.sleep(0.3)
                servo1.ChangeDutyCycle(0)
                time.sleep(2)
                print ("servo1 90°")
        f = open('/home/pi/Desktop/Anis/pythonProject1/myCSVfile.csv', "w+")
        f.close()
        
        
        