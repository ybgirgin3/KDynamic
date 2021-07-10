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


def tc(env, data, wm):
    extra.theme_change(env, data, wm)
    #print('tc')

## variables
def wc(env):
    extra.wallp_change(env, os.path.join(plight, random.choice([p for p in os.listdir(plight)])))
    #print('wc')

def light_theme(env, theme, wm):
    print('light mode activating.. ')

    # theme change
    #os.system("kvantummanager --set {}".format(theme))
    tc(env, theme, wm)

    # change pic
    wc(env)

"""
if __name__ == '__main__':
    light_theme(input('env: '), input('theme: '))
"""
# end file
