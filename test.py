
import time
import json
import urllib.request
import subprocess
from subprocess import Popen
import urllib
import random
import os.path

while True:
    print("Check Audio")
    try:
        domain = "https://awiclass.monoame.com/"
        url = domain+"audiodeliver/get_music.php"
        wp = urllib.request.urlopen(url)
        pw = wp.read()
        data = json.loads(pw.decode("utf-8") )

        aid = -(int(random.random()*2)+1)
        #aid = -1
        print(data[aid])


        filename = "./audio/"+data[aid]['file'].split("/")[-1]
        #downloadname = "./audio"+data[aid]['file'].split("/")[-1]
        #if os.path.isfile(filename)==False:

        urllib.request.urlretrieve(domain+"audiodeliver"+data[aid]['file'],filename)
        subprocess.call(["omxplayer","--vol","800",filename])

    except error:
        print(str(error))

    time.sleep(10)
