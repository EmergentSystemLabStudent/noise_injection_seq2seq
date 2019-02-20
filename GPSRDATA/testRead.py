
import random
import sys
import copy
import os
import pandas as pd
import string
import base64
import json
import wave
import math

rooms = []

for room in [line.strip('\n') for line in open('rooms.txt', 'r').readlines()]:
    if room != '': #データないなら飛ばす
        if room[0] != '#':
            room = room.replace(' ', '')
            print (room)
            rooms.append(room)
