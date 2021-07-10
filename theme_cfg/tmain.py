# !/usr/bin/python3

"""
author: 'Yusuf Berkay Girgin'
created at 8 August 2021 09.01 Turkey/Sakarya
for using gnome desktop
"""

from themes import themer#, light_dark_theme, night_theme   # light theme module
from datetime import datetime
from pathlib import Path
import time
import json
import os

# ## hours
# ## --------> first hour, last hour
# lightHours = [7, 15]
# ## --------> last hour (light_dark's first hour is lights' last hour)
# lightDarkHours = [19, 21]
# ## --------> middle hour, last hour
# nightHours = [23, 6]

# hours = [7, 15, 19, 21, 23, 6]

## common minutes
#  --------> 0   1   2   3
# minutes = [0, 29, 30, 59]

# read paths and files
h = Path.home()
#env_spec_dir = os.path.join(h, "KDynamic", "theme", open(d_env, 'r').readline().strip())
d = os.path.join(h, "KDynamic")
#env_file = open(d + "/d_env.txt").readline().strip().upper()
# env_spec_dir = os.path.join(d, 'theme', env_file)
env_spec_dir = os.path.join(d, 'theme')
#t_json = json.load(os.path.join(env_spec_dir, 'themes.json'))
f = open(os.path.join(env_spec_dir, 'themes.json'))
data = json.load(f)

def main():
    try:
        # returns current hour as a integer
        currentHour = datetime.now().hour
        env = data['env']
        wm = data['wm']
        # currentHour = 18

        ## light theme
        if currentHour >= int(data['light_h']) and currentHour < int(data['light_dark_h']):
            print('light mode activating.. ')
            theme = data['light_t']
        
        ## light_dark theme
        elif currentHour >= int(data['light_dark_h']) and currentHour < int(data['night_h']):
            print('light dark mode activating.. ')
            theme = data['light_dark_t']


        # night theme
        elif currentHour >= int(data['night_h']) or currentHour >= 0 and currentHour < int(data['light_h']):
            print('night mode activating.. ')
            theme = data['night_t']


        themer(env, theme, wm)
        

    except KeyboardInterrupt as e:
        from sys import exit
        exit(0)

main()

