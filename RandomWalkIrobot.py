# -*- coding: utf-8 -*-
"""Created on Fri Nov 29 19:23:56 2019
@author: Aldo"""
import RPi.GPIO as GPIO
import time
from pycreate2 import Create2
import random

port = '/dev/ttyUSB0'
bot = Create2(port)
bot.start()
bot.full()
s2 =23
s3=24
signal = 25
NUM_CYCLES=5000

GPIO.setmode(GPIO.BCM)
GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.setup(s2,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(s3,GPIO.OUT)
print("\n")
columna=1
fila=1
azul=0
List_Izqnot =[1,2,4]
List_Dernot = [1,2,3]
List_Arrnot = [2,3,4]
List_Atrnot = [1,3,4]
Esq_NE = [2,3]
Esq_NO = [2,4]
Esq_SE = [1,3]
Esq_SO = [1,4]
#bot.stop()
a=0
funcion=0
while(1):
    sw=0
   
    if azul==1:
        bot.stop()
    if (columna==1 and fila==1):#Esquina Inferior Izq
        print("Esquina inferior izquierda")
        while(sw==0 or funcion==a):
            sw=1
            funcion = random.choice(Esq_SO)
        if funcion==1:
            bot.drive_straight(100)
            time.sleep(3.4)
            print("Adelante")
            fila = fila +1
            a=2
            bot.drive_stop()
            time.sleep(1)
        if funcion==4:
            bot.drive_turn(-75, 1)
            time.sleep(2.1)
            bot.drive_straight(100)
            time.sleep(3.1)
            bot.drive_turn(75, 1)
            time.sleep(2.1)
            print("Derecha")
            columna = columna +1
            a=3
            bot.drive_stop()
            time.sleep(1)
    elif (columna==6 and fila==6):#Esquina Superior Derecha
        print("Esquina Superior Derecha")
        while(sw==0 or funcion==a):
            sw=1
            funcion = random.choice(Esq_NE)
        if funcion==2:
            bot.drive_straight(-100)
            time.sleep(3.4)
            print("Atras")
            fila = fila - 1
            a=1
            bot.drive_stop()
            time.sleep(1)
        if funcion==3:
            bot.drive_turn(75, 1)
            time.sleep(2.1)
            bot.drive_straight(100)
            time.sleep(3)
            bot.drive_turn(-75, 1)
            time.sleep(2.1)
            print("Izquierda")
            columna = columna -1  
            a=4
            bot.drive_stop()
            time.sleep(1)
    elif (columna==1 and fila==6): #Esquina superior izquierda
        print("esquina Superior Izquierda")
        while(sw==0 or funcion==a):
            sw=1
            funcion = random.choice(Esq_NO)
        if funcion==2:
            bot.drive_straight(-100)
            time.sleep(3.4)
            print("Atras")
            fila = fila - 1
            a=1
            bot.drive_stop()
            time.sleep(1)
        if funcion==4:
            bot.drive_turn(-75, 1)
            time.sleep(2.1)
            bot.drive_straight(100)
            time.sleep(3.1)
            bot.drive_turn(75, 1)
            time.sleep(2.1)
            print("Derecha")
            columna = columna +1
            a=3
            bot.drive_stop()
            time.sleep(1)
    elif (columna==6 and fila==1): #Esquina inferior derecha
        print("Esquina inferior derecha")
        while(sw==0 or funcion==a):
            sw=1
            funcion = random.choice(Esq_SE)
        if funcion==1:
            bot.drive_straight(100)
            time.sleep(3.4)
            print("Adelante")
            fila = fila +1
            a=2
            bot.drive_stop()
            time.sleep(1)
        if funcion==3:
            bot.drive_turn(75, 1)
            time.sleep(2.1)
            bot.drive_straight(100)
            time.sleep(3)
            bot.drive_turn(-75, 1)
            time.sleep(2.1)
            print("Izquierda")
            columna = columna -1  
            a=4
            bot.drive_stop()
            time.sleep(1)
    elif (columna == 1 or columna ==6): #Esta en los bordes
        print("Esta en los bordes verticales")
        if columna==1:
            while(sw==0 or funcion==a):
                sw=1
                funcion = random.choice(List_Izqnot)
            if funcion==1:
                bot.drive_straight(100)
                time.sleep(3.4)
                print("Adelante")
                fila = fila +1
                a=2
                bot.drive_stop()
                time.sleep(1)
            if funcion==2:
                bot.drive_straight(-100)
                time.sleep(3.4)
                print("Atras")
                fila = fila - 1
                a=1
                bot.drive_stop()
                time.sleep(1)
            if funcion==4:
                bot.drive_turn(-75, 1)
                time.sleep(2.1)
                bot.drive_straight(100)
                time.sleep(3.1)
                bot.drive_turn(75, 1)
                time.sleep(2.1)
                print("Derecha")
                columna = columna +1
                a=3
                bot.drive_stop()
                time.sleep(1)
        elif columna==6:
            while(sw==0 or funcion==a):
                sw=1
                funcion = random.choice(List_Dernot)
            if funcion==1:
                bot.drive_straight(100)
                time.sleep(3.4)
                print("Adelante")
                fila = fila +1
                a=2
                bot.drive_stop()
                time.sleep(1)
            if funcion==2:
                bot.drive_straight(-100)
                time.sleep(3.4)
                print("Atras")
                fila = fila - 1
                a=1
                bot.drive_stop()
                time.sleep(1)
            if funcion==3:
                bot.drive_turn(75, 1)
                time.sleep(2.1)
                bot.drive_straight(100)
                time.sleep(3)
                bot.drive_turn(-75, 1)
                time.sleep(2.1)
                print("Izquierda")
                columna = columna -1  
                a=4
                bot.drive_stop()
                time.sleep(1)
    elif (fila==1 or fila==6):
        print("Esta en bordes horizontales")
        if fila==1:
            while(sw==0 or funcion==a):
                sw=1
                funcion = random.choice(List_Atrnot)
            if funcion==1:
                bot.drive_straight(100)
                time.sleep(3.4)
                print("Adelante")
                fila = fila +1
                a=2
                bot.drive_stop()
                time.sleep(1)
            if funcion==3:
                bot.drive_turn(75, 1)
                time.sleep(2.1)
                bot.drive_straight(100)
                time.sleep(3)
                bot.drive_turn(-75, 1)
                time.sleep(2.1)
                print("Izquierda")
                columna = columna -1  
                a=4
                bot.drive_stop()
                time.sleep(1)
            if funcion==4:
                bot.drive_turn(-75, 1)
                time.sleep(2.1)
                bot.drive_straight(100)
                time.sleep(3.1)
                bot.drive_turn(75, 1)
                time.sleep(2.1)
                print("Derecha")
                columna = columna +1
                a=3
                bot.drive_stop()
                time.sleep(1)
        elif fila==6:
            while(sw==0 or funcion==a):
                sw=1
                funcion = random.choice(List_Arrnot)
       
            if funcion==2:
                bot.drive_straight(-100)
                time.sleep(3.4)
                print("Atras")
                fila = fila - 1
                a=1
                bot.drive_stop()
                time.sleep(1)
            if funcion==3:
                bot.drive_turn(75, 1)
                time.sleep(2.1)
                bot.drive_straight(100)
                time.sleep(3)
                bot.drive_turn(-75, 1)
                time.sleep(2.1)
                print("Izquierda")
                columna = columna -1  
                a=4
                bot.drive_stop()
                time.sleep(1)
            if funcion==4:
                bot.drive_turn(-75, 1)
                time.sleep(2.1)
                bot.drive_straight(100)
                time.sleep(3.1)
                bot.drive_turn(75, 1)
                time.sleep(2.1)
                print("Derecha")
                columna = columna +1
                a=3
                bot.drive_stop()
                time.sleep(1)
               
    else: #Si no esta ni en bordes ni esquinas
        print("no esta ni en bordes ni en esquinas")
        while(sw==0 or funcion==a):
            sw=1
            funcion = random.randrange(1,4)
        if funcion==1:
            bot.drive_straight(100)
            time.sleep(3.4)
            print("Adelante")
            fila = fila +1
            a=2
            bot.drive_stop()
            time.sleep(1)
        if funcion==2:
            bot.drive_straight(-100)
            time.sleep(3.4)
            print("Atras")
            fila = fila - 1
            a=1
            bot.drive_stop()
            time.sleep(1)
        if funcion==3:
            bot.drive_turn(75, 1)
            time.sleep(2.1)
            bot.drive_straight(100)
            time.sleep(3)
            bot.drive_turn(-75, 1)
            time.sleep(2.1)
            print("Izquierda")
            columna = columna -1  
            a=4
            bot.drive_stop()
            time.sleep(1)
        if funcion==4:
            bot.drive_turn(-75, 1)
            time.sleep(2.1)
            bot.drive_straight(100)
            time.sleep(3.1)
            bot.drive_turn(75, 1)
            time.sleep(2.1)
            print("Derecha")
            columna = columna +1
            a=3
            bot.drive_stop()
            time.sleep(1)
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    red  = NUM_CYCLES / duration   #in Hz
    azul=0
    print(red)
    if red<12000 and red>9400:
        print("azul")
        print(red)
        azul=0                            
    print("fila es =",fila)
    print("columna es =",columna)
    bot.drive_stop()
    time.sleep(1)
