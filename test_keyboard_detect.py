import keyboard #Using module keyboard
import threading
import time
def func1():
    while 1:
         if keyboard.is_pressed('a'): 
            print('You Pressed: a')
            time.sleep(1)
def func2():
    while 1:
         if keyboard.is_pressed('b'): 
            print('You Pressed: b')
            time.sleep(1)
def func3():
    while 1:
         if keyboard.is_pressed('c'): 
            print('You Pressed: c')
            time.sleep(1)
def func4():
     print('quang huy')
            
f1 = threading.Thread(target=func1)
f2 = threading.Thread(target=func2)
f3 = threading.Thread(target=func3)
f4 = threading.Thread(target=func4)
f1.start()
f2.start()
f3.start()
f4.start()
f1.join()
f2.join()
f3.join()
f4.join()

while True:
    pass
