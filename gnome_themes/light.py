# !/usr/bin/python3
# Filename: light.py
import os
from pathlib import Path
import random
import sys
sys.path.insert('..')
from extra import extra

# configure for gnome themes
#homedir = os.path.expanduser('~')
h = Path.home()
#env_spec_dir = os.path.join(h, "KDynamic", "theme", open(d_env, 'r').readline().strip())

# pic paths
plight = os.path.join(h, "KDynamic", "pics", 'light')
#env_file = open(d + "/d_env.txt").readline().strip().upper()
#env_spec_dir = os.path.join(d, 'theme', env_file)
#t_json = open(os.path.join(env_spec_dir, 'themes.json'),)


## variables
def wc(env):

    extra.wallp_change(env, random.choice([p for p in os.listdir(plight)]))

def tc(data):
    extra.theme_changer(env, data)


def light(env, theme):
    print('light mode activating.. ')

    # theme change
    #os.system("kvantummanager --set {}".format(theme))
    tc(env, data)

    # change pic
    wc(env)

# end file
