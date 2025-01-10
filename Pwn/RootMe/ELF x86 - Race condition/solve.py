#!/usr/bin/env python3

import threading
import subprocess

def challange():
    for i in range(1, 6):
        args = ("./chall")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()

def catfile():
    for i in range(1, 6):
        args = ("/bin/cat", "/tmp/tmp_file.txt")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        output = popen.stdout.read()
        print(output)

challthread = threading.Thread(target=challange)
catthread = threading.Thread(target=catfile)

challthread.start()
catthread.start()

challthread.join()
catthread.join()
