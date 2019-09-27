# !/usr/bin/python3
# Filename: night.py
import random
import os


homedir = os.path.expanduser('~')
kvantum_pic_night_theme = '{}/KDynamic/Pictures/night/night.txt'.format(homedir)
kvantum_night_plasma_theme = '{}/KDynamic/Kvantum/night_kvantum_plasma.txt'.format(homedir)


one_time = []

## night theme
def night():
    print('night mode activating -- wallpapers changing')

    ## change wallpaper
    # reads .txt file from specified folder
    # recommended folder path is '/home/<user>/Pictures/"Theme Changer"/night/night.txt'
    with open(kvantum_pic_night_theme, 'r') as f:
        r = f.readlines()
        for line in r:
            one_time.append(line)

    randomLine = random.choice(one_time)
    os.system(randomLine)

    with open(kvantum_night_plasma_theme, 'r') as f:
        r = f.readlines()
        for line in r:
            os.system("kvantummanager --set {}".format(line))

    ## avoiding overwriting
    one_time.clear()

# night()
# end file
