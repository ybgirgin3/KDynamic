# !/usr/bin/python3
# Filename: light_dark.py
import random
import time
import os

homedir = os.path.expanduser('~')
light_dark_txt = '{}/KDynamic/Pictures/light_dark/light_dark.txt'.format(homedir)
light_plasma_theme = '{}/KDynamic/Kvantum/light_plasma_theme.txt'.format(homedir)
night_plasma_theme = '{}/KDynamic/Kvantum/night_plasma_theme.txt'.format(homedir)
one_time = []

## light_dark theme
def plasma_themes(txt_file):
    with open(txt_file, 'r') as f:
        r = f.readlines()
        for line in r:
            # os.system("kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name {}".format(line))
            os.system("kvantummanager --set {}".format(line))


def light_dark(isDark=None):
    print('light_dark mode activating -- wallpaper changing')

    ## change wallpaper
    # reads .txt file from specified folder
    # recommended folder path is '/home/<user>/Pictures/"Theme Changer"/night/night.txt'
    with open(light_dark_txt, 'r') as f:
        r = f.readlines()
        for line in r:
            one_time.append(line)

    randomLine = random.choice(one_time)

    ## plasma theme will be black in the second half of light_dark theme
    ## controlling isDark boolean

    ### bu kısım kendi içinde de ikiye ayrıldığı için bununda light
    ### ve dark temaları ayrı ayrı klasörlenip tanımlanmalı
    if not isDark:
        ### white theme
        ## specified light plasma theme
        # os.system("kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name Mojave-light")
        plasma_themes(light_plasma_theme)
        time.sleep(1)
        os.system(randomLine)
        print('isDark = False')

    elif isDark:
        ### black theme
        # print('light_dark theme activating -- black plasma')
        ## specified dark plasma theme
        # os.system("kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name McMojave")
        plasma_themes(night_plasma_theme)
        time.sleep(1)
        os.system(randomLine)
        print('isDark = True')


    one_time.clear()

#
