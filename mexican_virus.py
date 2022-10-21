import time
import random as rnd
import os
import linecache
from pygame import mixer

mixer.init()
mixer.music.load('files/shadowfiend.mp3')
mixer.music.play()

n = 1000


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    

for i in range(101):
    time.sleep(rnd.random() * 0.05)
    clear()
    print("Installing mexican virus: " + str(i) + "%")
    m = rnd.randint(0, 10)
    k = 0
    if m <= 1:
        with open('files/file.txt') as f:
            lines = list(f)
        for i in range(rnd.randint(0, 7)):
            time.sleep(rnd.random() * 0.225)
            print(rnd.choice(lines))
            

clear()
time.sleep(1)

for i in range(3):
    time.sleep(0.5)
    print("Mexican virus installed successfully")
    time.sleep(1)
    clear()

time.sleep(1.5)

while n - 7 >= 0:
    print(n)
    n = n - 7
    time.sleep(rnd.random() * 0.2)
    if n < 25:
        print(n)
        n = n - 7
        time.sleep(rnd.random() * 1)
        if n - 14 <= 0:
            print(n)
            n = n - 7
            time.sleep(2)

print(n)
time.sleep(1.5)
clear()
time.sleep(0.5)

for i in range(5):
    time.sleep(rnd.random() * 0.1)
    print(n-7)
    time.sleep(rnd.random() * 0.3)
    clear()

time.sleep(2)
clear()
time.sleep(0.5)

for i in range(101):
    time.sleep(rnd.random() * 0.05)
    clear()
    print("Initializing hard disk drive formatting: " + str(i) + "%")
    k = 0
    m = rnd.randint(0, 9)
    if m <= 2:    
        while k <= 19:
            a = rnd.randint(0, 1024)
            print(str(chr(a)), end='')
            k = rnd.randint(0,20)
        clear()

time.sleep(2)
clear()

for i in range(5):
    time.sleep(rnd.random() * 0.3)
    print("ты быдло")
    time.sleep(rnd.random() * 0.5)
    clear()
    if i == 3:
        time.sleep(rnd.random() * 0.2)
        print("ты быдло")
        time.sleep(rnd.random() * 0.6)
        clear()
        time.sleep(rnd.random() * 0.8)
    elif i == 4:
        time.sleep(rnd.random() * 0.4)
        print("нет, ты мой друг")
        time.sleep(rnd.random() * 1.5)
        clear()
    
time.sleep(1.5)
for i in range(115):
    clear()
    n = rnd.randint(0, 20)
    k = 0
    print('дима с днем рождения')
    time.sleep(0.1)
    if n <= 4:
        clear()
        while k <= 17:
            a = rnd.randint(0, 1024)
            print(str(chr(a)), end='')
            k = rnd.randint(0,20)


while (mixer.music.get_busy()):
    a = rnd.randint(0, 1024)
    print(str(chr(a)), end='')

clear()
print("мяу")
time.sleep(2)
