
from pygame import mixer
import time
import vlc
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

    import urllib
    urllib.request.urlretrieve ("http://192.168.8.200/audiodeliver/"+data[-1]['file'],data[-1]['file'])

    #print(data)
    subprocess.call(["omxplayer", data[-1]['file']])

    time.sleep(6)
