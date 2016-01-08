from turtle import *
from time import sleep
import explorerhat
import easygui as eg

def fwd(screen,move):
    forward(screen)
    explorerhat.motor.one.forwards(60)
    explorerhat.motor.two.forwards(40)
    sleep(move)
    explorerhat.motor.stop()
    

def l(screen,move):
    left(screen)
    explorerhat.motor.one.backwards(60)
    explorerhat.motor.two.forwards(40)
    sleep(move)
    explorerhat.motor.stop()

def r(screen,move):
    right(screen)
    explorerhat.motor.one.forwards(60)
    explorerhat.motor.two.backwards(40)
    sleep(move)
    explorerhat.motor.stop()

def rev(screen,move):
    backward(screen)
    explorerhat.motor.one.backwards(60)
    explorerhat.motor.two.backwards(40)
    sleep(move)
    explorerhat.motor.stop()

def square():
    for i in range(4):
        fwd(100,1)
        l(90,0.4)
    done()    

def star():
    for i in range(5):
        fwd(100,1)
        r(144,0.4)
    done()

def hexagon():
    for i in range(6):
        fwd(100,1)
        left(60,0.2)
    done()

try:
    while True:
        choice = eg.choicebox(title="Robot-Artist",msg="Choose a pattern to draw",choices=("square","star","hexagon"))
        if choice == "square":
            square()
        elif choice == "star":
            star()
        elif choice == "hexagon":
            hexagon()
        else:
            break
except KeyboardInterrupt:
    eg.msgbox(title="Program Exit",msg="Thanks for playing")
