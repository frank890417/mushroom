
import time
import json
import urllib.request
import subprocess
from subprocess import Popen
import urllib
import random
import os.path
counter = 0
while True:
    print("Check Audio #"+str(counter))


    counter=counter+1
    if (counter>100):
        subprocess.call(["sudo","reboot"])
    try:
        domain = "https://techart.cc/"
        url = domain+"audiodeliver/get_music.php"
        wp = urllib.request.urlopen(url)
        pw = wp.read()
        data = json.loads(pw.decode("utf-8") )

        aid = -(int(random.random()*4)+1)
        #aid = -1
        print(data[aid])


        filename = "./audio/"+data[aid]['file'].split("/")[-1]
        #downloadname = "./audio"+data[aid]['file'].split("/")[-1]
        #if os.path.isfile(filename)==False:
        try:
            urllib.request.urlretrieve(domain+"audiodeliver"+data[aid]['file'],filename)
            subprocess.call(["omxplayer","--vol","800",filename])
        except:
            #print(str(e))
            continue # continue to next row

    except:
        #print(str(error))
        continue
    time.sleep(8)
