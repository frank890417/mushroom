
#from pygame import mixer
import time
#import vlc
import json
import urllib.request
import subprocess

import urllib

while True:

    print("Check Audio")
    url = "http://192.168.8.200/audiodeliver/get_music.php"
    wp = urllib.request.urlopen(url)
    pw = wp.read()
    #print(pw.decode("utf-8")
    data = json.loads(pw.decode("utf-8") )
    print(data[-1])

    urllib.request.urlretrieve ("http://192.168.8.200/audiodeliver"+data[-1]['file'],"./audio/"+data[-1]['file'].split("/")[-1])

    #print(data)
    subprocess.call(["omxplayer", "/audio/"+data[-1]['file'].split("/")[-1] ])

    time.sleep(6)
