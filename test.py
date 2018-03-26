
from pygame import mixer
import time
import pygame
import vlc
#p = vlc.MediaPlayer("http://your_mp3_url")
#p.play()
import json
import urllib.request
import subprocess
pygame.mixer.pre_init(44100, 0, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
pygame.mixer.init()

import urllib

while True:
    
    print("Check Audio")
    url = "http://192.168.8.200/audiodeliver/get_music.php"
    wp = urllib.request.urlopen(url)
    pw = wp.read()
    #print(pw.decode("utf-8")
    data = json.loads(pw.decode("utf-8") )
    print(data[-1])

    import urllib
    urllib.request.urlretrieve ("http://192.168.8.200/audiodeliver/"+data[-1]['file'],data[-1]['file'])
    #p = vlc.MediaPlayer("http://192.168.8.200/audiodeliver/"+data[-1]['file'])
    #p.play()
    
    #print(data)
    subprocess.call(["omxplayer", data[-1]['file']]) 
    #subprocess.Popen("omxplayer \""+ data[-1]['file']+"\"")

    time.sleep(6)
    #pygame.mixer.music.load('test2.mp3')

    #pygame.mixer.music.play(1)

    #while pygame.mixer.music.get_busy(): 
    #    pygame.time.Clock().tick(10)
