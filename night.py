# !/usr/bin/python3
# Filename: light.py
import random
import os

homedir = os.path.expanduser('~')
night_txt_file = '{}/KDynamic/Pictures/night/night.txt'.format(homedir)
night_plasma_theme = '{}/KDynamic/night_plasma_theme.txt'.format(homedir)

one_time = []

## night theme
def night():
    print('night mode activating -- wallpapers changing')

    ## change wallpaper
    # reads .txt file from specified folder
    # recommended folder path is '/home/<user>/Pictures/"Theme Changer"/night/night.txt'
    with open(night_txt_file, 'r') as f:
        r = f.readlines()
        for line in r:
            one_time.append(line)

    randomLine = random.choice(one_time)
    os.system(randomLine)

    # os.system("kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name McMojave")
    with open(night_plasma_theme, 'r') as f:
        r = f.readlines()
        for line in r:
            os.system("kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name {}".format(line))

    ## avoiding overwriting
    one_time.clear()

# night()
# end file
