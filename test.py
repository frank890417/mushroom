
import time
import json
import urllib.request
import subprocess
from subprocess import Popen
import urllib

while True:
    print("Check Audio")
    domain = "https://techart.nthu.edu.tw/THE2018/"
    url = domain+"audiodeliver/get_music.php"
    wp = urllib.request.urlopen(url)
    pw = wp.read()
    data = json.loads(pw.decode("utf-8") )

    print(data[-1])
    urllib.request.urlretrieve(domain+"audiodeliver"+data[-1]['file'],"./audio/"+data[-1]['file'].split("/")[-1])
    subprocess.call(["omxplayer", "./audio/"+data[-1]['file'].split("/")[-1] ])

    time.sleep(6)
