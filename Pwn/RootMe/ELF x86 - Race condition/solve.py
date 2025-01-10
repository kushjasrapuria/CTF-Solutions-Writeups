#!/usr/bin/env python3

import threading
import subprocess
import time

def challange():
    for i in range(1, 6):
        args = ("./chall")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        output = popen.stdout.read()

def catfile():
    for i in range(1, 6):
        args = ("/bin/cat", "/tmp/tmp_file.txt")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        output = popen.stdout.read()
        print(output)

thread1 = threading.Thread(target=challange)
thread2 = threading.Thread(target=catfile)


thread1.start()
thread2.start()

thread1.join()
thread2.join()
