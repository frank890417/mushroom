
import time
import json
import urllib.request
import subprocess
from subprocess import Popen
import urllib
import random
while True:
    print("Check Audio")
    domain = "https://techart.nthu.edu.tw/THE2018/"
    url = domain+"audiodeliver/get_music.php"
    wp = urllib.request.urlopen(url)
    pw = wp.read()
    data = json.loads(pw.decode("utf-8") )

    aid = -(int(random.random()*5)+1)
    print(data[aid])
    urllib.request.urlretrieve(domain+"audiodeliver"+data[aid]['file'],"./audio/"+data[aid]['file'].split("/")[-1])
    subprocess.call(["omxplayer", "./audio/"+data[aid]['file'].split("/")[-1] ])

    time.sleep(6)
