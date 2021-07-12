# !/usr/bin/python3
# Filename: light.py
import os
from pathlib import Path
import random
import sys
#sys.path.insert('..')
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils import utils

# configure for gnome themes
#homedir = os.path.expanduser('~')
h = Path.home()
#env_spec_dir = os.path.join(h, "KDynamic", "theme", open(d_env, 'r').readline().strip())

# pic paths
pic_base = os.path.join(h, "KDynamic", "pics")
plight = os.path.join(pic_base, 'light')
plight_dark = os.path.join(pic_base, 'light_dark')
pnight = os.path.join(pic_base, 'night')
#env_file = open(d + "/d_env.txt").readline().strip().upper()
#env_spec_dir = os.path.join(d, 'theme', env_file)
#t_json = open(os.path.join(env_spec_dir, 'themes.json'),)


def tc(env, data, wm):
    utils.theme_change(env, data, wm)
    #print('tc')

## variables
def wc(env, ts):
    pd = ""
    if ts == 'light':
        pd = plight
    elif ts == 'light_dark':
        pd = plight_dark
    elif ts == 'night':
        pd = pnight
    
    print("image path: ",os.path.join(pd, random.choice([p for p in os.listdir(pd)])))
    utils.wallp_change(env, os.path.join(pd, random.choice([p for p in os.listdir(pd)])))
    #print('wc')

def themer(env, theme, wm, ts):

    # theme change
    #os.system("kvantummanager --set {}".format(theme))
    tc(env, theme, wm)

    # change pic
    wc(env, ts)
    
    
"""
if __name__ == '__main__':
    light_theme(input('env: '), input('theme: '))
"""
# end file
