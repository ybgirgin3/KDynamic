# !/usr/bin/python3
# Filename: light.py
import os
import random

homedir = os.expanduser('~')
light_txt_file = '{}/KDynamic/Pictures/light/light.txt'.format(homedir)
light_plasma_theme = '{}/KDynamic/light_plasma_theme.txt'.format(homedir)

## variables
one_time_wallpapers = []
# one_time_plasma = []

def light():
    print('light mode activating.. ')

    ## change wallpapers
    ## find wallpapers directory
    with open(light_txt_file, 'r') as f:
        r = f.readlines()
        for line in r:
            one_time_wallpapers.append(line)

    randomLine = random.choice(one_time_wallpapers)

    # print(randomLine)
    os.system(randomLine)

    print('light theme')
    ## changing plasma theme
    # specified light theme plasma theme
    # os.system("kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name Mojave-light")
    with open(light_plasma_theme, 'r') as f:
        r = f.readlines()
        for line in r:
            # one_time_plasma.append(line)
            os.system("kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name {}".format(line))

    # clean the list
    # avoiding overwriting
    one_time_wallpapers.clear()

# end file
